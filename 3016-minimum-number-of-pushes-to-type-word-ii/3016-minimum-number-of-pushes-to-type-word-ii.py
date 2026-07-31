from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Count the frequency of each character
        freqs = sorted(Counter(word).values(), reverse=True)
        
        total_pushes = 0
        for i, freq in enumerate(freqs):
            # i // 8 determines the multiplier layer (0 for 1st-8th, 1 for 9th-16th, etc.)
            multiplier = (i // 8) + 1
            total_pushes += freq * multiplier
            
        return total_pushes