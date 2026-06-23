class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}
        for i in s: 
            hash_s[i] = hash_s.get(i, 0) + 1
        for p in t: 
            hash_t[p] = hash_t.get(p, 0) + 1
        if hash_s == hash_t:
            return True
        return False
        
        