class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        
        # Find the smallest power of 2 that is strictly greater than n, 
        # or find the bit-length boundary.
        # For n > 2, the number of unique XOR values is 2^bit_length(n) 
        # adjusted to the proper range boundary.
        return 1 << n.bit_length()