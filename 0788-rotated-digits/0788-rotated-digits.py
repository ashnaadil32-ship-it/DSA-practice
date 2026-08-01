class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid = {'0', '1', '2', '5', '6', '8', '9'}
        change = {'2', '5', '6', '9'}

        ans = 0

        for num in range(1, n + 1):
            s = str(num)

            if all(ch in valid for ch in s) and any(ch in change for ch in s):
                ans += 1

        return ans