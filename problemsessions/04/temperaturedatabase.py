from setavltree import BSTNode, SetAVLTree

class Measurement:
    def __init__(self, temp, date):
        self.key = date
        self.temp = temp

    def __str__(self):
        return "(%s;%s)" % (self.key, self.temp)
    
    def __repr__(self):
        return self.__str__()

class TemperatureDBNode(BSTNode):

    def subtree_update(A):
        super().subtree_update()

        # augmentations
        A.max_temp = A.item.temp
        A.min_date = A.max_date = A.item.key

        if A.left:
            A.min_date = A.left.min_date
            A.max_temp = max(A.max_temp, A.left.max_temp)
        
        if A.right:
            A.max_date = A.right.max_date
            A.max_temp = max(A.max_temp, A.right.max_temp)

        
    def subtree_max_in_range(A, d1, d2):
        # print('call stack max in range')
        # breakpoint()
        # we will use the min_date and max_date already augmented (so accessible in O(1))
        # from the A subtree

        # Case 1) disjoint
        if (A.max_date < d1) or (A.min_date > d2):
            return None
        
        # Case 2) A min date and max date contains the d1 and d2 range. It is already augmented the 
        # max temp, so this will be O(1) time
        if (A.min_date >= d1) and (A.max_date <= d2):
            return A.max_temp
        
        # Case 3) The partially overlap cases, so will need to recurse
        # get first temperatue in the range (the x point in the b) question )
        t = None
        if d1 <= A.item.key <= d2:
            t = A.item.temp

        # now recurse left to find max temp in left subtree
        # once found, compare to the temperatura in root x for that subtree
        if A.left:
            # print('A left exists')
            # print(A.item)
            # breakpoint()
            # it will eventually reach a partition of the tree in which the range will
            # be outside the bounds of the tree (min_date and max_date)
            # and exactly the Base case of disjoint will take care of this 
            t_left = A.left.subtree_max_in_range(d1, d2)
            if t_left:
                if t:
                    t = max(t, t_left)
                else:
                    t = t_left

        if A.right:
            # print('A right exists')
            # print(A.item)
            # breakpoint()
            # Once traversing down the tree via recursion reach a point in which should not be so much right in the tree
            # the base case for outisde the range will take care of it returning none
            t_right  = A.right.subtree_max_in_range(d1, d2)
            if t_right:
                if t:
                    t = max(t, t_right)
                else:
                    t = t_right

        return t


class TemperatureDB(SetAVLTree):
    def __init__(self):
        super().__init__(TemperatureDBNode)

    def record_temp(self, t, d):
        try:
            m = self.delete(d)
            t = max(t, m.temp)
        except:
            pass
        
        self.insert(Measurement(t,d))

    def max_in_range(self, d1, d2):
        return self.root.subtree_max_in_range(d1, d2)
    
# Example Usage
if __name__ == '__main__':

    dates = [x for x in range(1,16)]
    temperatures = [21, 24, 23, 28, 30, 17, 19, 26, 31, 11, 18, 10, 15, 9, 27]
    # measurements = [Measurement(d, t) for d, t in zip(dates, temperatures)]
    # print(measurements)

    db = TemperatureDB()
    for d, t in zip(dates, temperatures):
        db.record_temp(t, d)

    db.max_in_range(6,13)