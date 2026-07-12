class Solution:
    def findTheString(self, lcp: list[list[int]]) -> str:
        n = len(lcp)
        A = [0] * n
        curr_char_id = 1  # Use 1-indexed IDs for characters (1='a', 2='b', ...)
        
        # Step 1: Greedy Character Assignment
        for i in range(n):
            if A[i] == 0:
                # If we need more than 26 distinct characters, it's impossible
                if curr_char_id > 26:
                    return ""
                
                # Assign the current character ID to i and all positions matching i
                for j in range(i, n):
                    if lcp[i][j] > 0:
                        A[j] = curr_char_id
                curr_char_id += 1
                
        # Convert IDs back to a string structure
        # 1 -> 'a', 2 -> 'b', etc.
        s = "".join(chr(96 + A[i]) for i in range(n))
        
        # Step 2: Verification using DP matching rules
        # An LCP matrix must satisfy:
        # lcp[i][j] = (lcp[i+1][j+1] + 1) if s[i] == s[j] else 0
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                expected_lcp = 0
                if s[i] == s[j]:
                    if i + 1 < n and j + 1 < n:
                        expected_lcp = lcp[i + 1][j + 1] + 1
                    else:
                        expected_lcp = 1
                
                if lcp[i][j] != expected_lcp:
                    return ""
                    
        return s