class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        
        sum1 = sum(int(c) for c in num[:half] if c != '?')
        sum2 = sum(int(c) for c in num[half:] if c != '?')
        
        cnt1 = num[:half].count('?')
        cnt2 = num[half:].count('?')
        
        # If total '?' is odd, Alice always wins
        if (cnt1 + cnt2) % 2 != 0:
            return True
        
        # Bob wins ONLY if the difference in initial sums matches 
        # the required compensation from the difference in '?' counts.
        # Alice wins otherwise.
        return (sum1 - sum2) != 9 * (cnt2 - cnt1) // 2