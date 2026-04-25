class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def make_dict(x: str):
            res = {}
            for c in x:
                res[c] = res.get(c, 0) + 1
            return res
        return make_dict(s) == make_dict(t)
