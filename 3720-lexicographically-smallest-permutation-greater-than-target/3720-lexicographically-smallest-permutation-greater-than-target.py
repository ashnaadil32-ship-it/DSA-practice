class Solution(object):
    def lexGreaterPermutation(self, s, target):

        count = [0] * 26

        # Frequency of characters in s
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        temp = count[:]
        pos = -1

        # Find the rightmost position where
        # we can make the string greater
        for i in range(len(target)):

            idx = ord(target[i]) - ord('a')

            # Find smallest character greater than target[i]
            for j in range(idx + 1, 26):
                if temp[j] > 0:
                    pos = i
                    break

            # If target[i] is not available,
            # we cannot continue matching target
            if temp[idx] == 0:
                break

            temp[idx] -= 1

        if pos == -1:
            return ""

        # Build answer using original count
        ans = []

        # Keep target prefix same
        for i in range(pos):
            ans.append(target[i])
            count[ord(target[i]) - ord('a')] -= 1

        # Put the smallest character > target[pos]
        idx = ord(target[pos]) - ord('a')

        for j in range(idx + 1, 26):
            if count[j] > 0:
                ans.append(chr(j + ord('a')))
                count[j] -= 1
                break

        # Add remaining characters in sorted order
        for i in range(26):
            while count[i] > 0:
                ans.append(chr(i + ord('a')))
                count[i] -= 1

        return ''.join(ans)