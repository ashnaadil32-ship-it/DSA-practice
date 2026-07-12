class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # We can swap indices i and j if abs(i - j) == 2.
        # This implies that all characters at even positions can freely swap with each other,
        # and all characters at odd positions can freely swap with each other.
        # Therefore, s1 can be transformed into s2 if and only if:
        # 1. The sorted characters at even positions match between s1 and s2.
        # 2. The sorted characters at odd positions match between s1 and s2.
        
        # Split and sort even positions (0, 2, 4, ...)
        even_s1 = sorted(s1[0::2])
        even_s2 = sorted(s2[0::2])
        
        # Split and sort odd positions (1, 3, 5, ...)
        odd_s1 = sorted(s1[1::2])
        odd_s2 = sorted(s2[1::2])
        
        return even_s1 == even_s2 and odd_s1 == odd_s2