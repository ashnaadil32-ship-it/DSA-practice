class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        digit_sum = 0

        for ch in str(n):
            if ch != '0':
                x = x * 10 + int(ch)
                digit_sum += int(ch)

        return x * digit_sum