class Solution(object):
    def minOperations(self, s):

        pattern1 = 0  # starts with '0'
        pattern2 = 0  # starts with '1'

        for i in range(len(s)):
            expected1 = '0' if i % 2 == 0 else '1'
            expected2 = '1' if i % 2 == 0 else '0'

            if s[i] != expected1:
                pattern1 += 1

            if s[i] != expected2:
                pattern2 += 1

        return min(pattern1, pattern2)
        