class Solution:
    def isValid(self, s: str) -> bool:
        opposite_map = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for c in s: 
            if c in opposite_map.keys(): 
                stack.append(opposite_map[c])
            elif not stack or c != stack.pop():
                return False
        return not stack
