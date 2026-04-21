class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        i = 0
        p = 0
        nums.sort()
        for i in range(len(nums)): 
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            want = nums[i]*-1
            p, d = i+1, len(nums) - 1
            while p < d:
                res_sol = []
                if nums[p] + nums[d] == want: 
                    res_sol.append(nums[p])
                    res_sol.append(nums[d])
                    res_sol.append(nums[i])
                    res.append(res_sol) 
                    p += 1
                    d -= 1 
                    while p < d and nums[p] == nums[p-1]:
                        p+=1
                    while p < d and nums[d] == nums[d+1]:
                        d-=1
                elif nums[p] + nums[d] > want:
                    d-=1
                else:
                    p+=1
        return res

                

            
        