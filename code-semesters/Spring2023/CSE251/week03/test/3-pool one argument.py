import os
import time
import multiprocessing as mp

def func(name):
    time.sleep(0.5)
    print(f'{name}, {os.getpid()}')

if __name__ == '__main__':

    names = ['john', 'Mary', ' April', 'Murry', 'George']

    with mp.Pool(2) as p:
        
        results = p.map(func, names)

    print(results)