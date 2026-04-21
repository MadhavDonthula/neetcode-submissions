class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Approach: 
        # take nums and subtract by target.
        # if sum is in nums, return index with nums index being subtracted
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return []