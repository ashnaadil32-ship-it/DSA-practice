class Solution:
    def checkOnesSegment(self, s):
        found_zero = False

        for ch in s:
            if ch == '0':
                found_zero = True
            elif found_zero:
                return False

        return True