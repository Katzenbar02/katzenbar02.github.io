import queue

def bfs_shortest_path(graph, start_node, target_node):
    # Create an empty queue
    my_queue = queue.Queue()

    # Enqueue the start node
    my_queue.put(start_node)

    # Create an empty set to track visited nodes
    visited = set()

    # Create an empty dictionary to track the path
    path = {}

    # Mark the start node as visited
    visited.add(start_node)

    # Perform BFS
    while not my_queue.empty():
        node = my_queue.get()

        # Check if the target node is found
        if node == target_node:
            # Reconstruct the shortest path
            shortest_path = []
            while node != start_node:
                shortest_path.append(node)
                node = path[node]
            shortest_path.append(start_node)
            shortest_path.reverse()
            return shortest_path

        # Explore the neighbors of the current node
        for neighbor in graph[node]:
            if neighbor not in visited:
                my_queue.put(neighbor)
                path[neighbor] = node
                visited.add(neighbor)

    # If the target node is not reachable
    return []

# Test the function
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
shortest_path = bfs_shortest_path(graph, start_node, target_node)
print(shortest_path)  # Output: ['A', 'C', 'F']
