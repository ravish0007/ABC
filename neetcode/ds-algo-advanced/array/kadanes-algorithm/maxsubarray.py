class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxVal = nums[0]
        currMax = 0

        for num in nums:
            currMax = max(currMax, 0)
            currMax += num

            maxVal = max(currMax, maxVal)
        return maxVal
