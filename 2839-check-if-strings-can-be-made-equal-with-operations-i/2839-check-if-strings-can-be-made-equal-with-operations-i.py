class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # We can only swap indices i and j if abs(i - j) == 2.
        # This means indices with the same parity (even-even or odd-odd) can be swapped freely.
        # Therefore, s1 can be transformed into s2 if and only if:
        # 1. The characters at even positions (0 and 2) match in both strings.
        # 2. The characters at odd positions (1 and 3) match in both strings.
        
        # Check even indices (0 and 2)
        even_s1 = sorted([s1[0], s1[2]])
        even_s2 = sorted([s2[0], s2[2]])
        
        # Check odd indices (1 and 3)
        odd_s1 = sorted([s1[1], s1[3]])
        odd_s2 = sorted([s2[1], s2[3]])
        
        return even_s1 == even_s2 and odd_s1 == odd_s2