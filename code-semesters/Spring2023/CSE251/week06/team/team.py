"""
Course: CSE 251
Lesson Week: 06
File: team.py
Author: Brother Comeau

Purpose: Team Activity

Instructions:

- Implement the process functions to copy a text file exactly using a pipe

After you can copy a text file word by word exactly
- Change the program to be faster (Still using the processes)

"""

import multiprocessing as mp
from multiprocessing import Value, Process
import filecmp 

# Include cse 251 common Python files
from cse251 import *

def sender(pipe):
    """ function to send messages to other end of pipe """
    '''
    open the file
    send all contents of the file over a pipe to the other process
    Note: you must break each line in the file into words and
          send those words through the pipe
    '''
    with open(pipe.recv(), 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                pipe.send(word)


def receiver(pipe):
    """ function to print the messages received from other end of pipe """
    ''' 
    open the file for writing
    receive all content through the shared pipe and write to the file
    Keep track of the number of items sent over the pipe
    '''
    with open(pipe.recv(), 'w') as f:
        count = 0
        while True:
            word = pipe.recv()
            if word is None:
                break
            f.write(word + ' ')
            count += 1


def are_files_same(filename1, filename2):
    """ Return True if two files are the same """
    return filecmp.cmp(filename1, filename2, shallow = False) 


def copy_file(log, filename1, filename2):
    # TODO create a pipe 
    pipe = mp.Pipe()

    # TODO create variable to count items sent over the pipe
    items_sent = Value('i', 0)

    # TODO create processes 
    send_proc = Process(target=sender, args=(pipe[0],))
    receive_proc = Process(target=receiver, args=(pipe[1],))

    # TODO start processes 
    send_proc.start()
    receive_proc.start()

    # TODO wait for processes to finish
    send_proc.join()
    receive_proc.join()

    # TODO get the number of items sent over the pipe
    items_sent = items_sent.value

    stop_time = log.get_time()

    log.stop_timer(f'Total time to transfer content = {items_sent}: ')
    log.write(f'items / second = {items_sent / (stop_time - start_time)}')

    if are_files_same(filename1, filename2):
        log.write(f'{filename1} - Files are the same')
    else:
        log.write(f'{filename1} - Files are different')


if __name__ == "__main__": 

    log = Log(show_terminal=True)

    copy_file(log, 'gettysburg.txt', 'gettysburg-copy.txt')
    
    # After you get the gettysburg.txt file working, uncomment this statement
    # copy_file(log, 'bom.txt', 'bom-copy.txt')
