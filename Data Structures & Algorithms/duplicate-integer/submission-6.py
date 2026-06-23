class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        curr_nums = {}
        for i in nums: 
            if i in curr_nums:
                return True
            curr_nums[i] = 1
        return False
