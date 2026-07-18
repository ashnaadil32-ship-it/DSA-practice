class Solution:
    def reverse(self, n: int) -> int:
        reverse = 0
        sign = -1 if n < 0 else 1
        n = abs(n)
        
        while n > 0:
            last_digit = n % 10
            reverse = reverse * 10 + last_digit
            n = n // 10
        
        
        final_answer = reverse * sign
        
        
        if final_answer < -2**31 or final_answer > 2**31 - 1:
            return 0
            
        return final_answer