class Solution:
    def reverseBits(self, n: int) -> int:

        num = 0
        
        for i in range(32):
            num = num << 1
            num = num + (n & 1)
            n = n >> 1
   
        return num
