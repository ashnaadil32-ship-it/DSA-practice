class Solution:
    def binaryGap(self, n: int) -> int:
        max_gap = 0
        last_pos = -1
        current_pos = 0
        
        while n > 0:
            # Check if the lowest bit is a 1
            if n & 1:
                # If we have seen a 1 before, calculate the gap
                if last_pos != -1:
                    max_gap = max(max_gap, current_pos - last_pos)
                # Update the position of the last seen 1
                last_pos = current_pos
                
            # Move to the next bit
            n >>= 1
            current_pos += 1
            
        return max_gap