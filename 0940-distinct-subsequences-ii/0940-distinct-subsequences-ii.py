class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = [0] * 26
        total = 0

        for ch in s:
            idx = ord(ch) - ord('a')

            new_subseq = (total + 1) % MOD

            total = (total - dp[idx] + new_subseq) % MOD
            dp[idx] = new_subseq

        return total