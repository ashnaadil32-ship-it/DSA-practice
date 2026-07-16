import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:  # <-- Changed name here
        n = len(nums)
        prefixGcd = []
        
        # Step 1: Construct the prefixGcd array
        current_max = nums[0]
        for num in nums:
            current_max = max(current_max, num)
            prefixGcd.append(math.gcd(num, current_max))
            
        # Step 2: Sort prefixGcd in non-decreasing order
        prefixGcd.sort()
        
        # Step 3: Form pairs using two pointers from opposite ends
        total_sum = 0
        left = 0
        right = n - 1
        
        while left < right:
            total_sum += math.gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
            
        return total_sum