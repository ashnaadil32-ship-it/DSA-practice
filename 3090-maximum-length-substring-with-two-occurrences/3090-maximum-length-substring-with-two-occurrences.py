class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        count = {}
        
        for right in range(len(s)):
            char = s[right]
            count[char] = count.get(char, 0) + 1
            
            # If any character exceeds 2 occurrences, shrink the window from the left
            while count[char] > 2:
                count[s[left]] -= 1
                left += 1
                
            max_len = max(max_len, right - left + 1)
            
        return max_len