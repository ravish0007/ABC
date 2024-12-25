class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        globalMax = nums[0]
        globalMin = nums[0]
        total = 0
        currMax = 0
        currMin = 0

        for n in nums:
            total = total + n
            currMax = max(currMax+n, n)
            currMin = min(currMin+n, n)

            globalMax = max(globalMax, currMax)
            globalMin = min(globalMin, currMin)
        
        return max(globalMax, total - globalMin) if globalMax > 0 else globalMax
