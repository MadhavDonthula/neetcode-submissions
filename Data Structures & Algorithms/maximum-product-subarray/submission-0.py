class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        curMin, curMax = 1, 1

        for n in nums:
            if n == 0: 
                curMin, curMax = 1, 1 
                continue 
            tmp = curMax*n 
            curMax = max(curMin*n, curMax*n, n)
            curMin = min(curMin*n, tmp, n) #curMax gets changed in the line above 
            res = max(res, curMax)
        return res 

        
