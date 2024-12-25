class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        duplicate_removed = [nums[0]]
        for num in nums:
            if num != duplicate_removed[-1]:
                duplicate_removed.append(num)

        for x,j in enumerate(duplicate_removed):
            nums[x] = j


        return len(duplicate_removed)
