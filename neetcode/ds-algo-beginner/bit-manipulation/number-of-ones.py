class Solution:
    def hammingWeight(self, n: int) -> int:
        
        count = 0
        while n > 0:
            last_bit = n & 1
            if last_bit:
                count += 1
            n = n >> 1
        return count
