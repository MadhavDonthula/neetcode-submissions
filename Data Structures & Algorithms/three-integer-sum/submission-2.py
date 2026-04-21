class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        overall_hash = {}
        res = set()
        for i, num in enumerate(nums):
            overall_hash[i] = num * -1
        for k, v in overall_hash.items(): 
            arr = nums[:k] + nums[k+1:]
            check_arr = self.twoSum(arr, v)
            for pair in check_arr:
                triplet = sorted([nums[k], pair[0], pair[1]])
                res.add(tuple(triplet))
        return [list(x) for x in res]
        
    def twoSum(self, two_sum_nums, target):
        seen = set()
        pairs = []

        for t_num in two_sum_nums:
            check = target - t_num
            if check in seen: 
                pairs.append([check, t_num])
            seen.add(t_num)
        return pairs
        