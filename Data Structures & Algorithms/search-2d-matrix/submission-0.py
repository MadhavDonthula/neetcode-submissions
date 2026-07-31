class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        d_array = []
        for nums in matrix:
            for x in nums:
                d_array.append(x)
        L, R = 0, len(d_array) - 1 
        while L<=R:
            mid = L + (R-L) //2 
            if d_array[mid] > target: 
                R = mid -1 
            elif d_array[mid] < target: 
                L = mid + 1
            else: 
                return True
        return False