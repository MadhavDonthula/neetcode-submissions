class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        for i, num in enumerate(nums): 
            check = target - num
            if check in seen: 
                return [seen[check], i]
            seen[num] = i 
        