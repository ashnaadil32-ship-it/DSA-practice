class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(s):
            count = 0

            for ch in s:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        queue = [s]
        visited = {s}
        found = False
        ans = []

        while queue:
            curr = queue.pop(0)

            if is_valid(curr):
                ans.append(curr)
                found = True

            if found:
                continue

            for i in range(len(curr)):
                if curr[i] not in "()":
                    continue

                new = curr[:i] + curr[i + 1:]

                if new not in visited:
                    visited.add(new)
                    queue.append(new)

        return ans