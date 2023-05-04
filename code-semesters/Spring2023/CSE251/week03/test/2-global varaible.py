import threading
import multiprocessing as mp

global_var = 0

def func(name):
    global global_var
    global_var = 123456
    print(f'{name}: {global_var}')

if __name__ == '__main__':

    print(f'Before process global_var = {global_var}')