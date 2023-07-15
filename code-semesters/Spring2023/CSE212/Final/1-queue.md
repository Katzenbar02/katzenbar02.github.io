# Queue
A queue is a data structure that follows the "first-in, first-out" (FIFO) principle. It is an ordered collection of elements where new elements are added to the rear (end) of the queue and removal of elements occurs from the front (beginning) of the queue.

Here are some things that can be done because of queue:
1. Task scheduling and job processing
2. Implementing multi-threaded or multi-process communication
3. Implementing breadth-first search (BFS) or graph traversal algorithms
4. Implementing concurrent processing or parallel computing
5. Implementing caching and buffering mechanisms
## Queue operations
These operations form the basic interface for working with queues.

* `Enqueue`: This operation adds an element to the rear or end of the queue.
* `Dequeue`: This operation removes and returns the element from the front or beginning of the queue.
* `Peek`: This operation returns the element at the front of the queue without removing it.
* `Size`: This operation returns the number of elements currently present in the queue.
* `Empty`: This operation checks whether the queue is empty or not.


Here are some examples of queue operations:

```python
import queue

my_queue = queue.Queue()  # Create a new queue

# ENQUEUE
my_queue.put(10)  # Enqueue element 10
my_queue.put(20)  # Enqueue element 20
my_queue.put(30)  # Enqueue element 30

# DEQUEUE
element = my_queue.get()  # Dequeue element from the front
print(element)  # Output: The dequeued element

# FRONT
front_element = my_queue.queue[0]  # Peek at the front element
print(front_element)  # Output: The element at the front of the queue

# SIZE
queue_size = my_queue.qsize()  # Get the size of the queue
print(queue_size)  # Output: The size of the queue

# EMPTY
is_empty = my_queue.empty()  # Check if the queue is empty
print(is_empty)  # Output: True if the queue is empty, False otherwise
```

## Multithreading
A queue can be used in conjunction with multithreading to facilitate efficient communication and coordination between multiple threads.

The following shows how to use a queue to implement a producer-consumer pattern. The producer thread enqueues items in the queue, and the consumer thread dequeues items from the queue. The producer and consumer threads run concurrently, and the queue acts as a buffer between them.

```python
import queue
import threading

# Function to process items from the queue
def process_queue(q):
    while True:
        item = q.get()  # Dequeue an item from the queue
        if item is None:
            break  # Break the loop if a None item is encountered
        # Process the item (perform some task)
        print("Processing item:", item)
        # ...

# Create a queue
my_queue = queue.Queue()

# Create and start multiple threads
num_threads = 4
threads = []
for _ in range(num_threads):
    t = threading.Thread(target=process_queue, args=(my_queue,))
    t.start()
    threads.append(t)

# Enqueue items in the queue
items = [1, 2, 3, 4, 5]
for item in items:
    my_queue.put(item)

# Wait for all threads to finish
for _ in range(num_threads):
    my_queue.put(None)  # Enqueue None items to signal threads to exit
for t in threads:
    t.join()

```
## Example

In this example, we will use a queue to reverse a string. We will enqueue each character of the string into the queue and then dequeue each character from the queue to construct the reversed string.

```python
import queue

def reverse_string(input_string):
    # Create an empty queue
    my_queue = queue.Queue()

    # Enqueue each character into the queue
    for char in input_string:
        my_queue.put(char)

    # Create an empty string
    reversed_string = ""

    # Dequeue each character and append to the reversed string
    while not my_queue.empty():
        char = my_queue.get()
        reversed_string += char

    # Return the reversed string
    return reversed_string

# Test the function
input_str = "Hello, World!"
reversed_str = reverse_string(input_str)
print(reversed_str)  # Output: "!dlroW ,olleH"

```
## Problem to solve : Fastest path
Problem: Write a Breadth-First Search (BFS) algorithm to find the shortest path in a graph.

You are given a graph represented as an adjacency list and two nodes: a start node and a target node. Implement a function that performs a Breadth-First Search (BFS) to find the shortest path from the start node to the target node in the graph.

Example:

```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
start_node = 'A'
target_node = 'F'
```
The expected output for this example would be the shortest path from node 'A' to node 'F': ['A', 'C', 'F'].

To solve this problem, you can follow these steps:

1. Define a function, let's call it bfs_shortest_path, that takes the graph, start node, and target node as input.
2. Create an empty queue using queue.Queue().
3. Create an empty set to track visited nodes.
4. Enqueue the start node to the queue.
5. Create an empty dictionary to track the path from each node to its previous node.
6. While the queue is not empty:
* Dequeue a node from the front of the queue.
* If the dequeued node is the target node, reconstruct the shortest path using the path dictionary and return it.
* Otherwise, iterate through the neighbors of the dequeued node that have not been visited:
* Enqueue each unvisited neighbor to the queue.
* Add the dequeued node as the previous node for each unvisited neighbor in the path dictionary.
Mark each unvisited neighbor as visited.
7. If the target node is not reachable from the start node, return an empty list to indicate that there is no path.

You can check your code with the solution here: [Solution](1-queue.py)



[Back to Welcome Page](0-welcome.md)
