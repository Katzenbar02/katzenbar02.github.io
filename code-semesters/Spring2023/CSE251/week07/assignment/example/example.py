"""
Course: CSE 251
Lesson Week: 07
File: assingnment.py
Author:
Purpose: Process Task Files
Instructions:  See I-Learn
TODO
I created 5 pools to collect data. I believe that 5 would be perfect 
for a few reasons, but the mostly because we have 5 different calls. 
I thought it may be faster to add more, I remembered Amdahl's law,
and I was able to calculate for my 12 core system, roughly 
5 is accurate as well. Therefore, I'll stick to 5.
"""

from datetime import datetime, timedelta
import requests
import multiprocessing as mp
from matplotlib.pylab import plt
import numpy as np
import glob
import math 

# Include cse 251 common Python files - Dont change
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
    if is_prime(value) == True:
        print(f"Value: {value} is prime")
        return result_primes.append(value)
    else:
        return result_primes.append(f"{value} is not Prime!")
        

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
             return result_words.append(f'{word} Found')
        else:
            return result_words.append(f'{word} not found *****')
            
            

def task_upper(text):
    """
    Add the following to the global list:
        {text} ==>  uppercase version of {text}
    """
    return result_upper.append(text.upper())

def task_sum(start_value, end_value):
    """
    Add the following to the global list:
        sum of {start_value:,} to {end_value:,} = {total:,}
    """
    sum = 0
    for num in range(start_value, end_value + 1):
        sum = sum + num
    return result_sums.append(sum)

def task_name(url):
    """
    use requests module
    Add the following to the global list:
        {url} has name <name>
            - or -
        {url} had an error receiving the information
    """
    #fetch data from URL
    # for i in range(1, 84):
    url = [f"http://127.0.0.1:8790/people/2/"]
    result_names.append(url)

    

def main():
    log = Log(show_terminal=True)
    log.start_timer()

    # TODO Create process pools
    pool = mp.Pool(5)
   
    pool.apply_async(task_prime, args = (is_prime, ), callback = result_primes)
    
    # time.sleep(0.05)       # Do something - this is the main thread sleeping

    pool.apply_async(task_word, callback = result_words)

    # time.sleep(0.05)       # Do something

    pool.apply_async(task_upper, callback = result_upper)

    # time.sleep(1)       # Do something

    pool.apply_async(task_sum, callback = result_sums)

    # time.sleep(1)       # Do something

    pool.apply_async(task_name, callback = result_names)

    

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

    # TODO start and wait pools
    pool.close()
    pool.join()

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