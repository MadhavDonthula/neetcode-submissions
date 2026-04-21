class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def make_dict(x: str):
            res = {}
            for i in range(len(x)):
                res[x[i]] = res.get(x[i], 0) + 1
            return res
        return make_dict(s) == make_dict(t)
