from functools import cache

class Solution:
    def minimumDistance(self, word: str) -> int:
        n = len(word)
        
        # Helper function to compute the Manhattan distance between two letter indices
        def get_dist(char_idx1, char_idx2):
            if char_idx1 == 26 or char_idx2 == 26: 
                return 0 # Initial placement is free
            
            x1, y1 = divmod(char_idx1, 6)
            x2, y2 = divmod(char_idx2, 6)
            return abs(x1 - x2) + abs(y1 - y2)
            
        @cache
        def dp(i, f1, f2):
            # Base case: all letters typed
            if i == n:
                return 0
                
            # Convert current character to an index from 0 to 25
            curr_char_idx = ord(word[i]) - ord('A')
            
            # Choice 1: Use Finger 1 to type the current character
            cost1 = get_dist(f1, curr_char_idx) + dp(i + 1, curr_char_idx, f2)
            
            # Choice 2: Use Finger 2 to type the current character
            cost2 = get_dist(f2, curr_char_idx) + dp(i + 1, f1, curr_char_idx)
            
            return min(cost1, cost2)
            
        # Start typing from index 0. Both fingers begin at state 26 (unplaced/free).
        return dp(0, 26, 26)