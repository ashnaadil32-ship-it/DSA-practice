from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
            
        # 1. Your initial frequency map for p (you wrote this part well!)
        p_freq = {}
        for ch in p:
            p_freq[ch] = p_freq.get(ch, 0) + 1
            
        window_freq = {}
        res = []
        p_len = len(p)
        
        # 2. Sliding through s
        for i in range(len(s)):
            # Add current character to window
            ch = s[i]
            window_freq[ch] = window_freq.get(ch, 0) + 1
            
            # If window size exceeds p, remove the leftmost character
            if i >= p_len:
                left_ch = s[i - p_len]
                if window_freq[left_ch] == 1:
                    del window_freq[left_ch]
                else:
                    window_freq[left_ch] -= 1
                    
            # Check if current window matches the pattern frequencies
            if window_freq == p_freq:
                res.append(i - p_len + 1)
                
        return res