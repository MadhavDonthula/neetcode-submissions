class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while i < len(nums):
            x = 0
            while x < len(nums):
                if nums[i] + nums[x] == target and i != x:
                    return [i, x]
                else: 
                    x+=1

            i += 1
        
