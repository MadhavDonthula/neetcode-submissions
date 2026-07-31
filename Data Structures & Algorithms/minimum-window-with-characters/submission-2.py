class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t) > len(s):
            return ""
        hash_t = {}
        hash_s = {}
        for char in t: 
            hash_t[char] = hash_t.get(char, 0) + 1
        L = 0 
        formed = 0 
        length = float('inf')
        res = ""
        required = len(hash_t.keys())
        for R in range(len(s)): 
            if s[R] in hash_t: 
                hash_s[s[R]] = hash_s.get(s[R], 0) + 1
                if hash_s[s[R]] == hash_t[s[R]]:
                    formed +=1
            while formed == required: 
                if (R - L) + 1 < length:
                    res = s[L:R+1]
                    length = (R - L) + 1
                if s[L] in hash_t:
                    hash_s[s[L]] -= 1
                    if hash_s[s[L]] < hash_t[s[L]]:
                        formed -=1
                L+=1
        return res 
            

            






        

