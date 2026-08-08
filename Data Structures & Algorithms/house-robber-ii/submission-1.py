class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob1(tempNums):
            rob1, rob2 = 0, 0 
            for n in tempNums:
                temp = max(n+rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        return max(rob1(nums[1:]), rob1(nums[:-1]))
