class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_pattern = {}

        iter2 = s.split()
        
        if len(pattern) != len(iter2):
            return False
        
        for i in range(len(pattern)):
            char = pattern[i]
            if char in s_pattern: 
                if s_pattern[char] != iter2[i]:
                    return False
            elif iter2[i] in s_pattern.values(): 
                return False
            else: 
                s_pattern[char] = iter2[i]
        return True
