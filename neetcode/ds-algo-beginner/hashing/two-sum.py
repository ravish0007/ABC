class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i, x in enumerate(nums):
            if target - x in seen:
                return [seen[target-x], i]
            else:
                seen[x] = i
        
