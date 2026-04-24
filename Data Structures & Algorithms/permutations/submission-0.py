class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(layer):
            if not layer: 
                res.append(subset.copy())
                return 
            for i in range(len(layer)):
                subset.append(layer[i])

                dfs(layer[:i] + layer[i+1:])
                subset.pop()
                
            
        dfs(nums)
        return res

            


