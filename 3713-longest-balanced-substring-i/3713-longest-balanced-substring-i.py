from collections import Counter

class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 0
        
        # Enumerate every possible starting position
        for i in range(n):
            counts = Counter()
            max_freq = 0
            distinct_count = 0
            
            # Expand the substring to the right
            for j in range(i, n):
                char = s[j]
                counts[char] += 1
                
                # If this is the first time seeing this character
                if counts[char] == 1:
                    distinct_count += 1
                
                # Update the maximum frequency seen in the current substring
                max_freq = max(max_freq, counts[char])
                
                # Current substring length is (j - i + 1)
                # It's balanced if the unique character count * max frequency equals the length
                if max_freq * distinct_count == (j - i + 1):
                    max_len = max(max_len, j - i + 1)
                    
        return max_len        