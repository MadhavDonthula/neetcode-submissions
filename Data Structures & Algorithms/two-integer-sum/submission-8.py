class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i in range(len(nums)):
            check = target - nums[i]
            if check in res:
                return [res[check], i]
            res[nums[i]] = i
            



                
