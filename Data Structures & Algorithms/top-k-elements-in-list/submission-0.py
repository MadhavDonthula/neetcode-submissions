class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for i in nums: 
            res[i] = res.get(i, 0) + 1

        new_res = sorted(res.items(), key=lambda x: x[1], reverse=True)
        actual_res = []
        for p in new_res[0:k]:
            actual_res.append(p[0])
        return actual_res
