class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        curr = 0
        for i in range(len(nums) - 1):
            curr = nums[i]
            for x in nums[i+1:]:
                if curr == x:
                    return True
        return False