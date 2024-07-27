import heapq
import math

def generate_list_opinions(polls):
    # Create a min-heap to store the log2(n) animals with the strongest opinions
    min_heap = []

    # Iterate through the polls
    for poll in polls:
        name, opinion = poll
        abs_opinion = abs(opinion)

        # Check if the heap is not full or if the current poll has a larger absolute opinion
        if len(min_heap) < math.log2(len(polls)):
            heapq.heappush(min_heap, (abs_opinion, name))
        elif abs_opinion > min_heap[0][0]:
            heapq.heappushpop(min_heap, (abs_opinion, name))

    # Extract names from the heap
    result = [animal[1] for animal in min_heap]

    return result
