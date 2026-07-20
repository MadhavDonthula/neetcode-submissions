class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        overall_hash = {}
        res = set()
        for i,  num in enumerate(nums):
            overall_hash[i] = num * - 1
        for k, v in overall_hash.items():
            arr = nums[:k] + nums[k+1:]
            check_arr = self.twoSum(arr, v)
            for pair in check_arr:
                sort_trip = sorted([v*-1, pair[0], pair[1]])
                res.add(tuple(sort_trip))
        return [list(x) for x in res]


    def twoSum(self, numberlist, target):
        seen = set()
        pairs = []
        for t_num in numberlist : 
            if target - t_num in seen: 
                pairs.append([target-t_num, t_num])
            seen.add(t_num)
        return pairs
            