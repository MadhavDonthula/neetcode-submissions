import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        res = 0
        for num in nums: 
            heapq.heappush(maxHeap, -1 * num)
        for i in range(k):
            res = -1 * heapq.heappop(maxHeap)
        return res
