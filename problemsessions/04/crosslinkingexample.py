import bisect

class CrossLinkedArray:

    '''Using 3 data structures to keep one in sorted order, another in sorted order, and another to keep the pointer from one to another using a hash'''
    
    def __init__(self):
        self.ids = []       # Array to store user IDs (sorted)
        self.scores = []    # Array to store corresponding scores (sorted)
        self.linked_data = {}  # Dictionary to link IDs and scores

    def add_user(self, user_id, score):
        # Insert ID in sorted order
        index = bisect.bisect_left(self.ids, user_id)
        self.ids.insert(index, user_id)

        # Insert score in sorted order
        score_index = bisect.bisect_left(self.scores, score)
        self.scores.insert(score_index, score)

        # Link ID and score
        self.linked_data[user_id] = score

    def get_score(self, user_id):
        # Retrieve score using binary search on IDs
        index = bisect.bisect_left(self.ids, user_id)
        if 0 <= index < len(self.ids) and self.ids[index] == user_id:
            return self.linked_data[user_id]
        else:
            return None

# Example usage
user_data = CrossLinkedArray()

# Add users with IDs and scores
user_data.add_user(101, 85)
user_data.add_user(102, 92)
user_data.add_user(104, 78)
user_data.add_user(105, 95)

# Retrieve scores based on user IDs
print("Score for user 102:", user_data.get_score(102))
print("Score for user 104:", user_data.get_score(104))
print("Score for user 106:", user_data.get_score(106))
