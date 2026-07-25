class Solution:
    def maxProduct(self, n: int) -> int:
        n = str(n)
        max1 = max2 = -1
        for digits in n:
            d = int(digits)
            if d > max1:
                max2 = max1
                max1 = d
            elif d > max2 :
                max2 = d

                    
        return max1 * max2