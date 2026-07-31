class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap_s1 = {}
        hashmap_s2 = {}
        for x in s1: 
            hashmap_s1[x] = hashmap_s1.get(x, 0) + 1
        for y in s2[0: len(s1) - 1]: 
            hashmap_s2[y] = hashmap_s2.get(y, 0) + 1
        
        max_string = s1 if max(len(s1), len(s2)) == s1 else s2
        L = 0 
        for R in range(len(s1) -1, len(s2)):
            char_R = s2[R] 
            hashmap_s2[char_R] = hashmap_s2.get(char_R, 0) + 1
            if hashmap_s2 == hashmap_s1: 
                return True
            elif hashmap_s2[s2[L]] == 1:
                del hashmap_s2[s2[L]]
            else: 
                hashmap_s2[s2[L]] -= 1
            L += 1
        return False




            


        
        