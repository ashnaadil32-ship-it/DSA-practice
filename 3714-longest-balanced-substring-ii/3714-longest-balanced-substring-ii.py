class Solution:
    def longestBalanced(self, s: str) -> int:
        
        # --- CASE 1: Exactly 1 unique character ---
        # Look for consecutive blocks of identical characters.
        def calc1(s: str) -> int:
            res = 0
            i, n = 0, len(s)
            while i < n:
                j = i + 1
                while j < n and s[j] == s[i]:
                    j += 1
                res = max(res, j - i)
                i = j
            return res

        # --- CASE 2: Exactly 2 unique characters ---
        # The 3rd forbidden character 'z' acts as a boundary breaker.
        # We find subarrays containing ONLY 'a' and 'b' where frequency(a) == frequency(b).
        def calc2(s: str, a: str, b: str, z: str) -> int:
            res = 0
            i, n = 0, len(s)
            while i < n:
                # Skip any occurrences of the forbidden character
                while i < n and s[i] == z:
                    i += 1
                    
                # Standard prefix sum difference mapping: diff = count(a) - count(b)
                # If diff matches an earlier seen index, the window in between has equal 'a's and 'b's.
                pos = {0: i - 1}
                d = 0
                while i < n and s[i] != z:
                    d += 1 if s[i] == a else -1
                    if d in pos:
                        res = max(res, i - pos[d])
                    else:
                        pos[d] = i
                    i += 1
            return res

        # --- CASE 3: Exactly 3 unique characters ---
        # We track the difference between counts: (count(a)-count(b), count(b)-count(c))
        # If the tuple matches a past state, all three characters grew at an equal rate.
        def calc3(s: str) -> int:
            pos = {(0, 0): -1}
            cnt = [0, 0, 0]
            res = 0
            for i, c in enumerate(s):
                cnt[ord(c) - ord('a')] += 1
                diff = (cnt[0] - cnt[1], cnt[1] - cnt[2])
                if diff in pos:
                    res = max(res, i - pos[diff])
                else:
                    pos[diff] = i
            return res

        # Compute max length from all possible configurations
        case_1 = calc1(s)
        case_2 = max(
            calc2(s, 'a', 'b', 'c'), # Only 'a' and 'b'
            calc2(s, 'b', 'c', 'a'), # Only 'b' and 'c'
            calc2(s, 'a', 'c', 'b')  # Only 'a' and 'c'
        )
        case_3 = calc3(s)
        
        return max(case_1, case_2, case_3)