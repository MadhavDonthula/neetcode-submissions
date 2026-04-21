class Solution:
    def maxArea(self, heights: List[int]) -> int:
        sol = 0
        l, r = 0, len(heights) - 1 
        while l < r: 
            left = heights[l]
            right = heights[r]
            if min(left, right) * (r - l) > sol:
                sol = min(left, right) * (r - l)
            if min(left, right) == left:
                l+=1
            else:
                r-=1
        return sol



        