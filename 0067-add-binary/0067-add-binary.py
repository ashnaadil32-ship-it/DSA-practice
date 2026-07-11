class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        
        # Loop until both strings are exhausted and no carry remains
        while i >= 0 or j >= 0 or carry:
            total = carry
            
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
                
            # Append the remainder (0 or 1) to our result list
            res.append(str(total % 2))
            # Calculate the new carry (0 or 1)
            carry = total // 2
            
        # Since we added digits from right to left, reverse the result
        return "".join(reversed(res))