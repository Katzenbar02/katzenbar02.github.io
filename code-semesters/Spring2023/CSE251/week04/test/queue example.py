import queue as q

q.put('House')
q.put('Tree')
q.put('Farm')
q.put('Truck')

print(f'Size of queue')

if q.qsize() > 0:
    item = q.get()