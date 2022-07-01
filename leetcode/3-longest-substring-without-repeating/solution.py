class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_start = 0
        chars = {}
        substring_length = 0
        
        for window_end in range(len(s)):
            char = s[window_end]
            
            if char in chars:
                window_start = max(window_start, chars[char] + 1)
                
            chars[char] = window_end
            
            substring_length = max(substring_length, window_end - window_start + 1)
        return substring_length
