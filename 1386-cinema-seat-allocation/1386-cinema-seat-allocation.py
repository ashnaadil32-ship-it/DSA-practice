import collections
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        row_to_seats = collections.defaultdict(int)
        
        # Build the bitmask for each row with reservations
        for row, seat in reservedSeats:
            row_to_seats[row] |= (1 << (seat - 1))
            
        ans = 0
        
        # Masks for the three possible 4-person groupings
        # Left: seats 2-5 -> bits 1 to 4
        # Middle: seats 4-7 -> bits 3 to 6
        # Right: seats 6-9 -> bits 5 to 8
        left_mask = 0b0111100000   # seats 2, 3, 4, 5
        middle_mask = 0b0001111000 # seats 4, 5, 6, 7
        right_mask = 0b0000011110  # seats 6, 7, 8, 9
        all_sides_mask = 0b0111111110 # seats 2 through 9
        
        for seats in row_to_seats.values():
            # If neither left nor right blocks are blocked, we can fit 2 families
            if (seats & all_sides_mask) == 0:
                ans += 2
            # Otherwise, check if we can fit at least 1 family in left, middle, or right
            elif (seats & left_mask) == 0 or (seats & middle_mask) == 0 or (seats & right_mask) == 0:
                ans += 1
                
        # Add 2 families for all rows that had zero reservations
        ans += (n - len(row_to_seats)) * 2
        
        return ans