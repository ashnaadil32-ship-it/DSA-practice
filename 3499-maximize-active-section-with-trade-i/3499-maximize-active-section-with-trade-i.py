class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        baseline_ones = 0
        max_zeros_gain = 0
        prev_zeros_len = float('-inf')
        
        i = 0
        n = len(s)
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            
            block_len = j - i
            
            if s[i] == '1':
                baseline_ones += block_len
            else:
                max_zeros_gain = max(max_zeros_gain, prev_zeros_len + block_len)
                prev_zeros_len = block_len
            
            i = j
            
        return baseline_ones + max_zeros_gain