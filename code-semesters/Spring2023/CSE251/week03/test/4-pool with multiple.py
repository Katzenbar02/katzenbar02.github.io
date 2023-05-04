import os
import time
import multiprocessing as mp



for i in range(10):
    numbers.append((random.randint(1, 1000), (randint)))

    print(f'Numbers list: {numbers}')

    with mp.Pool(5) as p:
        p.map(add_two_numbers, numbers)
