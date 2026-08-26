class Solution(object):
    def shortestBeautifulSubstring(self, s, k):

        if s.count('1') < k:
            return ""
        
        ones_indices = [i for i, ch in enumerate(s) if ch == '1']
        
        min_len = float('inf')
        ans = ""
        
        for i in range(len(ones_indices) - k + 1):
            start = ones_indices[i]
            end = ones_indices[i + k - 1]
            
            sub = s[start : end + 1]
            curr_len = len(sub)
            
            if curr_len < min_len:
                min_len = curr_len
                ans = sub
            elif curr_len == min_len:
                if sub < ans:
                    ans = sub
                    
        return ans