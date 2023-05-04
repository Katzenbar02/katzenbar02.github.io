from datetime import datetime, timedelta
import threading

from cse251 import *

prime_count = 0
numbers_processed = 0

def is_prime(n: int):
    global numbers_processed
    numbers_processed  += 1

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


def process_range(start, end, step):
    global prime_count
    for i in range(start, end, step):
        if is_prime(i):
            prime_count += 1
            print(i, end=', ', flush=True)

if __name__ == '__main__':
    log = Log(show_terminal=True)
    log.start_timer()

    start = 10000000000
    range_count = 100007

    number_threads = 10
    threads = []
    thread_end = start + range_count + 1

    for i in range(number_threads):
        t = threading.Thread(target=process_range, args=(start + i, thread_end, number_threads))
        threads.append(t)

        for t in threads:
            t.start()

        for t in threads:
            t.join()

        log.write(f"Numbers processed = {numbers_processed}")
        log.write(f'Primes found = {prime_count}')
        log.stop_timer('Total time')
