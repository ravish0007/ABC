


class kthLargest:

    def __init__(self, nums, k):
        self.q = nums
        self.k = k
        heapq.heapify(self.q)
        while len(self.q) > k:
            heapq.heappop(self.q)

    def add(self, val):

        heapq.heappush(self.q, val)
        if len(self.q) > self.k:
            heapq.heappop(self.q)
        return self.q[0]
