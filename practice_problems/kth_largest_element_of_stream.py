import heapq 

class KthLargest:

    def __init__(self, k, nums):
        self.num = nums
        self.k = k 
        heapq.heapify(self.num) # O(n)
        while len(self.num) > k:
            heapq.heappop(self.num) 

    def add(self, val):
        heapq.heappush(self.num, val)
        if len(self.num) > self.k: 
            heapq.heappop(self.num) 
        print(self.num[0])
        return self.num[0] 

kthLargest = KthLargest(3, [4, 5, 8, 2])
kthLargest.add(3) #   // return 4
kthLargest.add(5) #  // return 5
kthLargest.add(10)#  // return 5
kthLargest.add(9) #   // return 8
kthLargest.add(4) #   // return 8