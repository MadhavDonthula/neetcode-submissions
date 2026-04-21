class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap_s1 = {}
        hashmap_s2 = {}

        for n in s1:
            hashmap_s1[n] = hashmap_s1.get(n, 0) + 1
        for p in s2[0: len(s1) - 1]:
            hashmap_s2[p] = hashmap_s2.get(p, 0) + 1
        
        L = 0 
        window = ""
        for R in range(len(s1) - 1, len(s2)):
            char_R = s2[R]
            hashmap_s2[char_R] = hashmap_s2.get(char_R, 0) + 1
            if hashmap_s2 == hashmap_s1: 
                return True 
            else: 
                temp_del = hashmap_s2[s2[L]] - 1
                if temp_del == 0: 
                    del hashmap_s2[s2[L]]
                else:
                    hashmap_s2[s2[L]] = temp_del
                L += 1
        return False
