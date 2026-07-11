class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        prev_group_len = 0
        curr_group_len = 1
        
        # Traverse the string starting from the second character
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                # If the character is the same, our current block grows
                curr_group_len += 1
            else:
                # If it changes, the previous block is complete. 
                # Add the min of the two blocks to our total count.
                ans += min(prev_group_len, curr_group_len)
                # Move current block size to previous, and reset current to 1
                prev_group_len = curr_group_len
                curr_group_len = 1
                
        # Don't forget to add the valid substrings from the final pair of groups
        ans += min(prev_group_len, curr_group_len)
        
        return ans