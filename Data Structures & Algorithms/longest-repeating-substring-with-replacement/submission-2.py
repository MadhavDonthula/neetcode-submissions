class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if s == "": 
            return 0 
        max_f = 0 
        hashmap = {}
        L = 0
        res = 0
        for R in range(len(s)):
            hashmap[s[R]] = hashmap.get(s[R], 0) + 1
            max_f = max(max_f, hashmap[s[R]])
            length = ((R-L) + 1) - max_f 
            if length <= k: 
                res = max((R-L) + 1, res)
            else: 
                hashmap[s[L]] -=1 
                L +=1
        return res
            


            
            


                


        