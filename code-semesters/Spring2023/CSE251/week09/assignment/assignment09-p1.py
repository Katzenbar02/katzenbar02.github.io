"""
Course: CSE 251 
Lesson Week: 09
File: assignment09-p1.py 
Author: Joshua Ludwig

Purpose: Part 1 of assignment 09, finding a path to the end position in a maze

Instructions:
- Do not create classes for this assignment, just functions.
- Do not use any other Python modules other than the ones included.

"""
import math
from screen import Screen
from maze import Maze
import cv2
import sys

# Include cse 251 files
from cse251 import *

SCREEN_SIZE = 800
COLOR = (0, 0, 255)
SLOW_SPEED = 100
FAST_SPEED = 1
speed = SLOW_SPEED

def solve_path(maze, pos=None):
    """ Solve the maze and return the path. The path is a list of positions, (x, y) """
    if pos is None:
        pos = maze.get_start_pos()

    path = []
    (prow, pcol) = pos
    moves = maze.get_possible_moves(prow, pcol)

    if len(moves) == 0:
        if maze.at_end(prow, pcol):
            return [(prow, pcol)]
        else:
            return []

    for (mrow, mcol) in moves:
        maze.move(mrow, mcol, COLOR)
        possible_path = solve_path(maze, (mrow, mcol))
        if len(possible_path) == 0:
            maze.restore(mrow, mcol)
        else:
            path = [(prow, pcol)]
            path.extend(possible_path)
            return path

    return path


def get_path(log, filename):
    """ Get path for a maze file """
    global speed

    # create a Screen Object that will contain all of the drawing commands
    screen = Screen(SCREEN_SIZE, SCREEN_SIZE)
    screen.background((255, 255, 0))

    maze = Maze(screen, SCREEN_SIZE, SCREEN_SIZE, filename)

    path = solve_path(maze)

    log.write(f'Number of drawing commands for = {screen.get_command_count()}')

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

    return path


def find_paths(log):
    """ Find paths for maze files """
    files = [
        'verysmall.bmp',
        'verysmall-loops.bmp',
        'small.bmp',
        'small-loops.bmp',
        'small-odd.bmp',
        'small-open.bmp',
        'large.bmp',
        'large-loops.bmp'
    ]

    log.write('*' * 40)
    log.write('Part 1')

    for filename in files:
        log.write()
        log.write(f'File: {filename}')
        path = get_path(log, filename)
        log.write(f'Found path has length          = {len(path)}')

    log.write('*' * 40)


def main():
    """ Main function """
    sys.setrecursionlimit(5000)
    log = Log(show_terminal=True)
    find_paths(log)


if __name__ == "__main__":
    main()
