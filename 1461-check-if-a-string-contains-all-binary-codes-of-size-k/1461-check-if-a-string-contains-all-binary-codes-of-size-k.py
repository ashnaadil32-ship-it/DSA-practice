class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # There are 2^k total unique combinations
        required_count = 1 << k
        seen_codes = set()
        
        # Slide a window of size k across the string
        for i in range(len(s) - k + 1):
            substring = s[i:i + k]
            seen_codes.add(substring)
            
            # Early exit optimization: if we found all combinations, stop early
            if len(seen_codes) == required_count:
                return True
                
        return False