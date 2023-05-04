import threading

def thread_func(filename, count, lock):
    with lock:
        f = open(filename, 'w')
        f.write(str(count))
        f.close()

if __name__ == '__main__':

    lock = threading.Lock()

    t1 = threading.Thread(target=thread_func, args=('data.txt', 100, lock))
    t2 = threading.Thread(target=thread_func, args=('data.txt', 1, lock))

    t1.start()
    t2.start()

    t1.join()
    t2.join()