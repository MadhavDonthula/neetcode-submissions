class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_res = 0 
        L, R = 0, len(heights)-1
        while L < R: 
            curr_area = (R-L) * min(heights[L], heights[R])
            max_res = max(max_res, curr_area)
            if heights[L] < heights[R]: 
                L +=1
            elif heights[L] >= heights[R]: 
                R -=1
        return max_res