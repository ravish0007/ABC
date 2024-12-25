class Solution:


    def climbStairs(self, n: int) -> int:

        cache = {}
        def stuff(x):

            if x == n:
                return 1
            
            if x > n:
                return 0
            
            if x in cache:
                return cache[x]
            
            val = stuff(x+1) + stuff(x+2)
            cache[x] = val
            return val
            
        return stuff(0)
