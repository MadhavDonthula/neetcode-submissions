class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        current = []
        for i in nums:
            if i in current:
                return True
            current.append(i)
        return False
