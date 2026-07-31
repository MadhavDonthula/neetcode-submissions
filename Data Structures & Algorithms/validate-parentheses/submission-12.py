class Solution:
    def isValid(self, s: str) -> bool:
        opposite_map = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for x in s: 
            if x in opposite_map.keys():
                stack.append(opposite_map[x])
            elif not stack or stack[-1] != x: 
                return False
            else:
                stack.pop()
        if not stack: 
            return True
        return False


