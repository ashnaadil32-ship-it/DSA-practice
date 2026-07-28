class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        # Sort the first half of the string to get the smallest characters upfront
        sorted_half = sorted(s[:n // 2])
        
        # If length is odd, keep the middle character; otherwise leave it empty
        mid_char = [s[n // 2]] if n % 2 == 1 else []
        
        # Combine the sorted left half, middle character (if any), and the reversed left half
        return "".join(sorted_half + mid_char + sorted_half[::-1])