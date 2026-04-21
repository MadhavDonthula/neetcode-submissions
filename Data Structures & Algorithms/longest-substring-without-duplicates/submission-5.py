class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        
        left_pointer = 0
        window = s[0]
        max_string = 1
        
        for right in range(1, len(s)):
            new_window = s[left_pointer:right+1]
            
            if s[right] in window:
                repeated_index = window.index(s[right])
                left_pointer = left_pointer + repeated_index + 1
                window = s[left_pointer:right+1]
            else:
                window = new_window
            
            if len(window) > max_string:
                max_string = len(window)
        
        return max_string