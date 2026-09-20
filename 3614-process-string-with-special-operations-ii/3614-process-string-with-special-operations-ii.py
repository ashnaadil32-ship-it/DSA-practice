class Solution:
    def processStr(self, s: str, k: int) -> str:
        length = 0

        # Step 1: Calculate final length
        for ch in s:
            if ch == "#":
                length *= 2
            elif ch == "%":
                pass
            elif ch == "*":
                if length > 0:
                    length -= 1
            else:
                length += 1

        if k >= length:
            return "."

        # Step 2: Traverse backwards
        for ch in reversed(s):
            if ch == "#":
                prev = length // 2

                if k >= prev:
                    k -= prev

                length = prev

            elif ch == "%":
                k = length - 1 - k

            elif ch == "*":
                length += 1

            else:
                if k == length - 1:
                    return ch

                length -= 1

        return "."