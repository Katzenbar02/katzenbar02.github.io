"""
------------------------------------------------------------------------------
Course: CSE 251
Lesson Week: 03
File: assignment.py
Author: <Joshua Ludwig>

Purpose: Video Frame Processing

Instructions:

- Follow the instructions found in Canvas for this assignment
- No other packages or modules are allowed to be used in this assignment.
  Do not change any of the from and import statements.
- Only process the given MP4 files for this assignment

------------------------------------------------------------------------------
"""
from matplotlib.pylab import plt  # load plot library
from PIL import Image
import numpy as np
import timeit
import multiprocessing as mp

# Include cse 251 common Python files
from cse251 import *

# 4 more than the number of cpu's on your computer
CPU_COUNT = mp.cpu_count() + 4  

# Frames processed
FRAME_COUNT = 300

RED   = 0
GREEN = 1
BLUE  = 2

# Creates a new image file from image_file and green_file
def create_new_frame(image_file, green_file, process_file):


    # this print() statement is there to help see which frame is being processed
    print(f'{process_file[-7:-4]}', end=',', flush=True)

    image_img = Image.open(image_file)
    green_img = Image.open(green_file)

    # Make Numpy array
    np_img = np.array(green_img)

    # Mask pixels 
    mask = (np_img[:, :, BLUE] < 120) & (np_img[:, :, GREEN] > 120) & (np_img[:, :, RED] < 120)

    # Create mask image
    mask_img = Image.fromarray((mask*255).astype(np.uint8))

    image_new = Image.composite(image_img, green_img, mask_img)
    image_new.save(process_file)

# Processes the specified number of frames using the specified number of CPUs
def process_frames(frame_count, cpu_count):

    with mp.Pool(processes=cpu_count) as pool:
        image_numbers = range(1, frame_count+1)
        image_files = [rf'elephant/image{number:03d}.png' for number in image_numbers]
        green_files = [rf'green/image{number:03d}.png' for number in image_numbers]
        process_files = [rf'processed/image{number:03d}.png' for number in image_numbers]

        start_time = timeit.default_timer()
        pool.starmap(create_new_frame, zip(image_files, green_files, process_files))
        return timeit.default_timer() - start_time


if __name__ == '__main__':
    # single_file_processing(300)
    # print('cpu_count() =', cpu_count())

    all_process_time = timeit.default_timer()
    log = Log(show_terminal=True)

    xaxis_cpus = []
    yaxis_times = []

    for cpu_count in range(1, CPU_COUNT+1):
        print(f'Testing with {cpu_count} CPU(s)')

        time = process_frames(FRAME_COUNT, cpu_count)

        xaxis_cpus.append(cpu_count)
        yaxis_times.append(time)

        log.write(f'Time to process {FRAME_COUNT} frames with {cpu_count} CPU(s): {time:.2f} seconds')

    log.write(f'Total Time for ALL processing: {timeit.default_timer() - all_process_time}')

    # create plot of results and also save it to a PNG file
    plt.plot(xaxis_cpus, yaxis_times, label=f'{FRAME_COUNT}')
    
    plt.title('CPU Core yaxis_times VS CPUs')
    plt.xlabel('CPU Cores')
    plt.ylabel('Seconds')
    plt.legend(loc='best')

    plt.tight_layout()
    plt.savefig(f'Plot for {FRAME_COUNT} frames.png')
    plt.show()
