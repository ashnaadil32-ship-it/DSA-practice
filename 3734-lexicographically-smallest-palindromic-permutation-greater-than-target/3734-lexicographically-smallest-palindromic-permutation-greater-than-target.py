class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        from collections import Counter

        n = len(s)
        cnt = Counter(s)

        odd = [c for c in cnt if cnt[c] % 2]

        if len(odd) > 1:
            return ""

        mid = odd[0] if odd else ""

        half = [0] * 26

        for i in range(26):
            ch = chr(ord('a') + i)
            half[i] = cnt[ch] // 2

        left = []

        def possible():
            temp = left[:]

            for i in range(25, -1, -1):
                temp += [chr(ord('a') + i)] * half[i]

            left_part = ''.join(temp)
            pal = left_part + mid + left_part[::-1]

            return pal > target

        for _ in range(n // 2):
            found = False

            for i in range(26):
                if half[i] == 0:
                    continue

                half[i] -= 1
                left.append(chr(ord('a') + i))

                if possible():
                    found = True
                    break

                left.pop()
                half[i] += 1

            if not found:
                return ""

        left = ''.join(left)
        ans = left + mid + left[::-1]

        return ans if ans > target else "" 