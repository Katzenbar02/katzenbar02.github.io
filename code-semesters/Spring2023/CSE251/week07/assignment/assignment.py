"""
Course: CSE 251
Lesson Week: 07
File: assingnment.py
Author: <Joshua Ludwig>
Purpose: Process Task Files

Instructions:  Assignment
The assignment files is found here, create_tasks.py file and server.py file. You also need to download the file words.txt and data.txt
Follow the instructions found in the assignment.py
When you submit your assignment code file, describe the size of each process pool for each task type and you determined the best size of that pool.
run the Python program create_tasks.py to create the task files.
There are 5 different tasks that need to be processed. Each task needs to have it's own process pool. The number of processes in each pool is up to you. However, your goal is to process all of the tasks as quicky as possible using these pools. You will need to try out different pool sizes.
The program will load a task one at a time and add it to the pool that is used to process that task type. You can't load all of the tasks into memory/list and then pass them to a pool.
You are required to use the function apply_async() for these 5 pools. You can't use map(), or any other pool function. You must use callback functions with the apply_async() statement.
Each pool will collect that results of their tasks into a global list. (ie. result_primes, result_words, result_upper, result_sums, result_names)
the task_* functions contain general logic of what needs to happen
Run the server.py program from a terminal/console program. Simply type python server.py. This server is the same one used for assignment 2. Refer to assignment 2's documention on how to start and use the server.
Do not use try...except statements

TODO

Add your comments here on the pool sizes that you used for your assignment and
why they were the best choices.

I have 8 logical processors on my computer so I reasoned that I would need to disperse them out
to where each logical processor would be more efficient depending on the task's complexity.
I decided to give 3 logical processors to the prime task, 1 to the word task, 1 to the upper task, 1 to the sum task,
and 2 to the name task. I decided to give the prime task 3 logical processors because it is the most complex task
and I wanted to give it the most resources to complete the task.
I was able to achieve the best results with this combination of processors.
"""


from datetime import datetime, timedelta
import requests
import multiprocessing as mp
from matplotlib.pylab import plt
import numpy as np
import glob
import math

# Include cse 251 common Python files - Don't change
from cse251 import *

TYPE_PRIME  = 'prime'
TYPE_WORD   = 'word'
TYPE_UPPER  = 'upper'
TYPE_SUM    = 'sum'
TYPE_NAME   = 'name'

# Global lists to collect the task results
result_primes = []
result_words = []
result_upper = []
result_sums = []
result_names = []

def is_prime(n: int):
    """Primality test using 6k+-1 optimization.
    From: https://en.wikipedia.org/wiki/Primality_test
    """
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def task_prime(value):
    """
    Use the is_prime() above
    Add the following to the global list:
        {value} is prime
            - or -
        {value} is not prime
    """
    # Check if value is prime
    if is_prime(value):
        result_primes.append(f'{value} is prime')
    else:
        result_primes.append(f'{value} is not prime')

def task_word(word):
    """
    search in file 'words.txt'
    Add the following to the global list:
        {word} Found
            - or -
        {word} not found *****
    """
    with open('words.txt', 'r') as file:
        words = file.read().splitlines()
        if word in words:
            result_words.append(f'{word} Found')
        else:
            result_words.append(f'{word} not found *****')

def task_upper(text):
    """
    Add the following to the global list:
        {text} ==>  uppercase version of {text}
    """
    result_upper.append(f'{text} ==> {text.upper()}')

def task_sum(start_value, end_value):
    """
    Add the following to the global list:
        sum of {start_value:,} to {end_value:,} = {total:,}
    """
    total = sum(range(start_value, end_value + 1))
    result_sums.append(f'sum of {start_value:,} to {end_value:,} = {total:,}')

def task_name(url):
    """
    use requests module
    Add the following to the global list:
        {url} has name <name>
            - or -
        {url} had an error receiving the information
    """

    response = requests.get(url)
    if response.status_code == 200:
        name = response.json()['name']
        result_names.append(f'{url} has name {name}')
    else:
        result_names.append(f'{url} had an error receiving the information')


def main():
    log = Log(show_terminal=True)
    log.start_timer()

    # Create process pools with appropriate sizes for each task type
    # I have 8 logical processors on my computer so the mp.pool should reflect that depedning on the intensity of the task
    # pool = mp.Pool(1)
    # Create process pools with appropriate sizes for each task type
    pool_primes = mp.Pool(3)
    pool_words = mp.Pool(1)
    pool_upper = mp.Pool(1)
    pool_sums = mp.Pool(1)
    pool_names = mp.Pool(2)

    pool_primes.apply_async(task_prime, args=(is_prime, ), callback=result_primes)
    pool_words.apply_async(task_word, callback=result_words)
    pool_upper.apply_async(task_upper, callback=result_upper)
    pool_sums.apply_async(task_sum, callback=result_sums)
    pool_names.apply_async(task_name, callback=result_names)



   
    count = 0
    task_files = glob.glob("*.task")
    for filename in task_files:
        # print()
        # print(filename)
        task = load_json_file(filename)
        print(task)
        count += 1
        task_type = task['task']
        if task_type == TYPE_PRIME:
            task_prime(task['value'])
        elif task_type == TYPE_WORD:
            task_word(task['word'])
        elif task_type == TYPE_UPPER:
            task_upper(task['text'])
        elif task_type == TYPE_SUM:
            task_sum(task['start'], task['end'])
        elif task_type == TYPE_NAME:
            task_name(task['url'])
        else:
            log.write(f'Error: unknown task type {task_type}')

    # Wait for all the processes to finish
    # Close the pools and wait for all tasks to complete
    pool_primes.close()
    pool_words.close()
    pool_upper.close()
    pool_sums.close()
    pool_names.close()
    pool_primes.join()
    pool_words.join()
    pool_upper.join()
    pool_sums.join()
    pool_names.join()

    # Do not change the following code (to the end of the main function)
    def log_list(lst, log):
        for item in lst:
            log.write(item)
        log.write(' ')
    
    log.write('-' * 80)
    log.write(f'Primes: {len(result_primes)}')
    log_list(result_primes, log)

    log.write('-' * 80)
    log.write(f'Words: {len(result_words)}')
    log_list(result_words, log)

    log.write('-' * 80)
    log.write(f'Uppercase: {len(result_upper)}')
    log_list(result_upper, log)

    log.write('-' * 80)
    log.write(f'Sums: {len(result_sums)}')
    log_list(result_sums, log)

    log.write('-' * 80)
    log.write(f'Names: {len(result_names)}')
    log_list(result_names, log)

    log.write(f'Number of Primes tasks: {len(result_primes)}')
    log.write(f'Number of Words tasks: {len(result_words)}')
    log.write(f'Number of Uppercase tasks: {len(result_upper)}')
    log.write(f'Number of Sums tasks: {len(result_sums)}')
    log.write(f'Number of Names tasks: {len(result_names)}')
    log.stop_timer(f'Finished processes {count} tasks')

if __name__ == '__main__':
    main()