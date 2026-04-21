from collections import deque

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = deque([])
        neg = deque([])
        for n in nums: 
            if n > 0: 
                pos.append(n)
            else:
                neg.append(n)
        res = []
        while pos or neg: 
            if pos: 
                res.append(pos.popleft())
            if neg: 
                res.append(neg.popleft())
        return res


            