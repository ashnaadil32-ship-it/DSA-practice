class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
            
        prev2 = 1  # Ways to reach step (i-2)
        prev1 = 2  # Ways to reach step (i-1)
        
        for _ in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
            
        return prev1