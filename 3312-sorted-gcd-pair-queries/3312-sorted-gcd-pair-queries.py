from collections import Counter
from itertools import accumulate
import bisect

class Solution:
    def gcdValues(self, nums: list[int], queries: list[int]) -> list[int]:
        max_num = max(nums)
        
        # cnt[x] represents how many times value x appears in nums
        cnt = Counter(nums)
        
        # count_divisors[d] will store how many elements in nums are divisible by d
        count_divisors = [0] * (max_num + 1)
        for d in range(1, max_num + 1):
            # Sum up occurrences of all multiples of d
            for multiple in range(d, max_num + 1, d):
                count_divisors[d] += cnt[multiple]
                
        # count_exact_gcd[g] stores the number of pairs with GCD exactly g
        count_exact_gcd = [0] * (max_num + 1)
        
        # Iterate backwards to easily subtract larger multiples
        for g in range(max_num, 0, -1):
            v = count_divisors[g]
            # Total pairs with divisor g
            total_pairs = v * (v - 1) // 2
            
            # Subtract pairs that have a strictly larger GCD (multiples of g)
            for larger_multiple in range(2 * g, max_num + 1, g):
                total_pairs -= count_exact_gcd[larger_multiple]
                
            count_exact_gcd[g] = total_pairs
            
        # Build prefix sum of the pair counts to locate queries efficiently
        prefix_sums = list(accumulate(count_exact_gcd))
        
        # Answer each query using binary search
        ans = []
        for q in queries:
            # We want to find the first index g where prefix_sums[g] > q
            idx = bisect.bisect_right(prefix_sums, q)
            ans.append(idx)
            
        return ans