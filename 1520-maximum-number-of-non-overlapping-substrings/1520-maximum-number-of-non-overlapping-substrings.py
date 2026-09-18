class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {}
        last = {}

        # First and last occurrence of every character
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        intervals = []

        # Try each character as the starting point
        for ch in first:
            l = first[ch]
            r = last[ch]
            i = l
            valid = True

            while i <= r:
                c = s[i]

                # This character appeared before l
                if first[c] < l:
                    valid = False
                    break

                # Expand interval if needed
                r = max(r, last[c])
                i += 1

            if valid:
                intervals.append((l, r))

        # Select maximum number of non-overlapping intervals
        intervals.sort(key=lambda x: x[1])

        ans = []
        end = -1

        for l, r in intervals:
            if l > end:
                ans.append(s[l:r + 1])
                end = r

        return ans