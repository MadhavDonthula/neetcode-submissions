class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = s.replace(" ", "").lower()
        L, R = 0, len(r) - 1 
        while L < R:
            if not r[L].isalnum():
                L += 1
            elif not r[R].isalnum():
                R -= 1
            elif r[L] != r[R]:
                return False
            else:
                L += 1
                R -= 1
        return True