class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        
        # Iterate through all 32 bits
        for _ in range(32):
            # Shift result to the left to make room for the next bit
            result <<= 1
            # Extract the least significant bit of n and add it to result
            result |= (n & 1)
            # Shift n to the right to process the next bit
            n >>= 1
            
        return result