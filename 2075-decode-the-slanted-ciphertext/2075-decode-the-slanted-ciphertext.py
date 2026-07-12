class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText
            
        # Calculate total columns in the grid layout
        cols = len(encodedText) // rows
        res = []
        
        # Traverse each diagonal starting from row 0, column j
        for j in range(cols):
            r, c = 0, j
            # Move diagonally down-right
            while r < rows and c < cols:
                # Map 2D coordinate (r, c) back to 1D index
                idx = r * cols + c
                res.append(encodedText[idx])
                r += 1
                c += 1
                
        # Join the characters and remove trailing padding spaces
        return "".join(res).rstrip()