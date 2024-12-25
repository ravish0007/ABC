class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        d = lambda x, y:  (x**2+y**2)**0.5

        r = defaultdict(list)

        h = []

        for x in points:
            dist = d(x[0], x[1]) 
            heapq.heappush(h, dist)
            r[dist].append(x)

        output = []
        for i in range(k):
            output.append(r[heapq.heappop(h)].pop())
        
        return output
