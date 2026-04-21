class Solution:
    def validPalindrome(self, s: str) -> bool:
        delete_used = False 
        L = 0 
        R = len(s) - 1
        
        while L < R:
            if not s[L].isalnum(): 
                L+=1
            if not s[R].isalnum():
                R-=1
            if s[L] != s[R]:
                if delete_used:
                    return False
                else: 
                    delete_used = True
                    skipL, skipR = s[L + 1: R+1], s[L:R]
                    return (skipL == skipL[::-1] or skipR == skipR[::-1])
            L+=1
            R-=1
        return True
