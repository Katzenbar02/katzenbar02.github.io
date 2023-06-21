"""
Course: CSE 251 
Lesson Week: 09
File: assignment09-p2.py 
Author: Joshua Ludwig

Purpose: Part 2 of assignment 09, finding the end position in the maze

Instructions:
- Do not create classes for this assignment, just functions.
- Do not use any other Python modules other than the ones included.
- Each thread requires a different color by calling get_color().


This code is not interested in finding a path to the end position,
However, once you have completed this program, describe how you could 
change the program to display the found path to the exit position.

What would be your strategy?  

I would need to keep track of the path that each thread takes in a list.
When a thread finds the end position, it is added to a list of paths.
Since each thread travels a different path, the path will sooner or later
be found.  Once the path is found, the program will stop all threads and
display the path.


Why would it work?

Each thread travels a different path, and a path will be contructed to the
end position using mutiple threads to find the end position. You can then
see the path that was created using the threads.


"""
import math
import threading 
from screen import Screen
from maze import Maze
import sys
import cv2

# Include cse 251 files
from cse251 import *

SCREEN_SIZE = 700
COLOR = (0, 0, 255)
COLORS = (
    (0,0,255),
    (0,255,0),
    (255,0,0),
    (255,255,0),
    (0,255,255),
    (255,0,255),
    (128,0,0),
    (128,128,0),
    (0,128,0),
    (128,0,128),
    (0,128,128),
    (0,0,128),
    (72,61,139),
    (143,143,188),
    (226,138,43),
    (128,114,250)
)
SLOW_SPEED = 100
FAST_SPEED = 0

# Globals
current_color_index = 0
thread_count = 0
stop = False
speed = SLOW_SPEED

def get_color():
    """ Returns a different color when called """
    global current_color_index
    if current_color_index >= len(COLORS):
        current_color_index = 0
    color = COLORS[current_color_index]
    current_color_index += 1
    return color

def solve_path(maze, start, color, path_found, lock):
    """ Find a path to the next dead end.
    When a fork is reached, spawn a new thread for every path except 1,
    and go down the remaining path.
    Push all created threads to threads.
    When a dead end is reached or path_found is True, die.
    When the end is reached, set path_found to True.
    """
    global thread_count
    with lock:
        thread_count += 1

    (row, col) = start
    while True:
        if path_found[0] or not maze.can_move_here(row, col):
            return
        with lock:
            maze.move(row, col, color)
        moves = maze.get_possible_moves(row, col)
        if len(moves) == 0:
            if maze.at_end(row, col):
                path_found[0] = True
            return
        elif len(moves) > 1:
            threads = []
            for i in range(len(moves) - 1):
                thread = threading.Thread(target=solve_path,
                                          args=(maze, moves[i], get_color(), path_found, lock))
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()

            (row, col) = moves[-1]
        else:
            (row, col) = moves[0]


def solve_find_end(maze):
    """ finds the end position using threads.  Nothing is returned """
    # When one of the threads finds the end position, stop all of them
    path_found = [False]
    start_pos = maze.get_start_pos()
    color = get_color()
    lock = threading.Lock()
    solve_path(maze, start_pos, color, path_found, lock)


def find_end(log, filename, delay):
    """ Do not change this function """

    global thread_count
    global speed

    # create a Screen Object that will contain all of the drawing commands
    screen = Screen(SCREEN_SIZE, SCREEN_SIZE)
    screen.background((255, 255, 0))

    maze = Maze(screen, SCREEN_SIZE, SCREEN_SIZE, filename, delay=delay)

    solve_find_end(maze)

    log.write(f'Number of drawing commands = {screen.get_command_count()}')
    log.write(f'Number of threads created  = {thread_count}')

    done = False
    while not done:
        if screen.play_commands(speed): 
            key = cv2.waitKey(0)
            if key == ord('1'):
                speed = SLOW_SPEED
            elif key == ord('2'):
                speed = FAST_SPEED
            elif key == ord('q'):
                exit()
            elif key != ord('p'):
                done = True
        else:
            done = True



def find_ends(log):
    """ Do not change this function """

    files = (
        ('verysmall.bmp', True),
        ('verysmall-loops.bmp', True),
        ('small.bmp', True),
        ('small-loops.bmp', True),
        ('small-odd.bmp', True),
        ('small-open.bmp', False),
        ('large.bmp', False),
        ('large-loops.bmp', False)
    )

    log.write('*' * 40)
    log.write('Part 2')
    for filename, delay in files:
        log.write()
        log.write(f'File: {filename}')
        find_end(log, filename, delay)
    log.write('*' * 40)


def main():
    """ Do not change this function """
    sys.setrecursionlimit(5000)
    log = Log(show_terminal=True)
    find_ends(log)



if __name__ == "__main__":
    main()