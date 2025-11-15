# Leetcode no.703 - Kth Largest Element in a Stream

import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        self.min_heap = nums
        self.k = k
        heapq.heapify(self.min_heap)
        
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)
        

    def add(self, val):
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]

# Example usage
if __name__ == "__main__":
    k = 3
    nums = [4, 5, 8, 2]
    kthLargest = KthLargest(k, nums)
    print(kthLargest.add(3))   # returns 4
    print(kthLargest.add(5))   # returns 5
    print(kthLargest.add(10))  # returns 5
    print(kthLargest.add(9))   # returns 8
    print(kthLargest.add(4))   # returns 8
     
        

