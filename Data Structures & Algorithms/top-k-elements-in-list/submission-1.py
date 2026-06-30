import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums: 
            freq[n] = freq.get(n, 0) + 1
        heap = []

        for p, v in freq.items():
            heapq.heappush(heap, (-v, p))

        res = []
        for i in range(min(k, len(heap))):
            res.append(list(heapq.heappop(heap))[1])
        return res
