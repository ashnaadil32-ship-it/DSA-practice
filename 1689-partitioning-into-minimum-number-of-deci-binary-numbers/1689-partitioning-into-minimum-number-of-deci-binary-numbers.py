class Solution:
    def minPartitions(self, n: str) -> int:
        # The answer is simply the largest single digit in the string
        return int(max(n))