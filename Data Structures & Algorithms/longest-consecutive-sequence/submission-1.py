class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = {}
        for i in nums:
            if i - 1 not in nums:
                res[i] = 1
                p = i + 1
                while p in nums: 
                    res[i] += 1
                    p += 1
        return max(res.values(), default=0)
                
        # [2, 3, 4, 4,5, 10, 20]

        
            


