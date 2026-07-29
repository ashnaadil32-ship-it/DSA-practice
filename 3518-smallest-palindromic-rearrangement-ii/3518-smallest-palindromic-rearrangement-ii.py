import collections
math_comb = __import__('math').comb

class Solution:
    def __init__(self):
        self.MAX = 10**6 + 1

    def smallestPalindrome(self, s: str, k: int) -> str:
        count = collections.Counter(s)
        
        # Extract half counts for the left portion of the palindrome
        half_count = [0] * 26
        mid_letter = ''
        for c, freq in count.items():
            idx = ord(c) - ord('a')
            half_count[idx] = freq // 2
            if freq % 2 == 1:
                mid_letter = c
                
        total_perm = self._calculateTotalPermutations(half_count)
        if k > total_perm:
            return ""
        
        # Greedily build the left half
        left_half = []
        half_len = sum(half_count)
        
        for _ in range(half_len):
            for i in range(26):
                if half_count[i] == 0:
                    continue
                
                # Temporarily choose character i
                half_count[i] -= 1
                arrangements = self._calculateTotalPermutations(half_count)
                
                if arrangements >= k:
                    left_half.append(chr(i + ord('a')))
                    break
                else:
                    k -= arrangements
                    half_count[i] += 1
                    
        return "".join(left_half) + mid_letter + "".join(reversed(left_half))

    def _calculateTotalPermutations(self, half_count: list[int]) -> int:
        total = sum(half_count)
        res = 1
        for freq in half_count:
            if freq > 0:
                res *= math_comb(total, freq)
                if res >= self.MAX:
                    return self.MAX
                total -= freq
        return res