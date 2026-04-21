class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)): 
            temp = nums.copy()
            temp.pop(i)
            sum = 1
            for p in range(len(temp)):
                sum *= temp[p]
            res.append(sum)
        return res





