class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        ans = 0
        
        for i in range(n):
            # i // 8 gives the multiplier level (0 for first 8, 1 for next 8, etc.)
            # We add 1 because pushes start at 1 instead of 0
            ans += (i // 8 + 1)
            
        return ans