class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        subset = []
        def dfs(i):
            if i >= len(nums):
                copy = sorted(subset.copy())
                res.add(tuple(copy))
                return 
            #decision to include nums[i]

            subset.append(nums[i])
            dfs(i+1)

            #decision not to include nums[i]
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return [list(x) for x in res]