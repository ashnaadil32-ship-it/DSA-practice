class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Base case: S_1 is always just "0"
        if n == 1:
            return "0"
        
        # Calculate the middle position of S_n
        mid = 1 << (n - 1)
        
        if k == mid:
            return "1"
        elif k < mid:
            # If k is in the left half, it's identical to the k-th bit of S_(n-1)
            return self.findKthBit(n - 1, k)
        else:
            # If k is in the right half, find the mirrored position in the left half
            # and invert the result ('0' <-> '1')
            mirrored_k = mid - (k - mid)
            corresponding_bit = self.findKthBit(n - 1, mirrored_k)
            return "1" if corresponding_bit == "0" else "0"