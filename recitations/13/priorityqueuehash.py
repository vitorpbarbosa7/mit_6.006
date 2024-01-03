# Hash table implementation of priority queue
class PriorityQueue:
    def __init__(self):
        # Store keys (distance to source vertex) with unique labels (vertex)
        self.A = {}

    def insert(self, label, key):
        self.A[label] = key

    def extract_min(self):
        min_label = None
        # Linear time on finding the minimum distance to source vertex
        for label in self.A:
            if (min_label is None) or (self.A[label] < self.A[min_label]):
                min_label = label
            # Remove the vertex from the priority queue 
        del self.A[min_label]
        # used for another iteration on relaxing adjacent vertices to this one
        return min_label

    def decrease_key(self, label, key):
        if (label in self.A) and (key < self.A[label]):
            self.A[label] = key