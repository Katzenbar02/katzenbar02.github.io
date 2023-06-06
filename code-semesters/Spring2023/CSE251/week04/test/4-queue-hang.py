from multiprocessing import Process, Queue

def f(q):
    q.put('x' * 1000)

if __name__ == '__main__':
    queue = Queue()
    p = Process(target=f, args=(queue,))
    p.start()
    print('before join')
    p.join()
    print('After join')
    obj = queue.get()
    print('After queue')