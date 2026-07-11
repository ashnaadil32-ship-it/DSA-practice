class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # We only need an array as large as the row we want to query
        row = [0.0] * (query_row + 1)
        row[0] = float(poured)
        
        # Simulate layer by layer
        for r in range(query_row):
            # Loop backwards to update the row in-place without overwriting needed data
            for c in range(r, -1, -1):
                if row[c] > 1.0:
                    overflow = row[c] - 1.0
                    half_overflow = overflow / 2.0
                    
                    # Split excess into the current spot (acts as bottom-left for next row)
                    # and the next spot (acts as bottom-right for next row)
                    row[c + 1] += half_overflow
                    row[c] = half_overflow
                else:
                    # If it doesn't overflow, it contributes 0 to the next row
                    row[c] = 0.0
                    
        return min(1.0, row[query_glass])
      