

def laststone(stones):
    q = heapq.heapify([-s for s in stones])

    while len(q) > 1:
        a, b = heapq.heappop(q), heapq.heappop(q)

        if b > a:
            heapq.heappush(q, a-b)

    return q[0]
