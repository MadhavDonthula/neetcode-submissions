class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if s == "": 
            return 0
        L = 0 
        window = ""
        hashmap = {}
        max_window=""
        for R in range(len(s)): 
            new_window = s[L:R+1]
            hashmap[s[R]] = hashmap.get(s[R], 0) + 1
            
            if len(new_window) - max(hashmap.values()) <= k: 
                window = new_window
                if len(window) > len(max_window): 
                    max_window = window
            else:
                hashmap[s[L]] = hashmap[s[L]] - 1
                L += 1
        return len(max_window)
            
 


        