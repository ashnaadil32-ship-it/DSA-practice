class Solution:
    def minOperations(self, s: str) -> int:
        ops_for_pattern_0 = 0
        
        for i, char in enumerate(s):
            # Pattern 0 expects '0' at even indices and '1' at odd indices
            if i % 2 == 0:
                if char != '0':
                    ops_for_pattern_0 += 1
            else:
                if char != '1':
                    ops_for_pattern_0 += 1
                    
        # Total operations for the alternate pattern is len(s) - ops_for_pattern_0
        ops_for_pattern_1 = len(s) - ops_for_pattern_0
        
        return min(ops_for_pattern_0, ops_for_pattern_1)