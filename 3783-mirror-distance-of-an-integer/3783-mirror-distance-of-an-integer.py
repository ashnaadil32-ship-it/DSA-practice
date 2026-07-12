class Solution:
    def mirrorDistance(self, n: int) -> int:
        original = n
        reversed_num = 0
        
        # Pop digits from the end of n and append them to reversed_num
        while n > 0:
            reversed_num = (reversed_num * 10) + (n % 10)
            n //= 10
            
        return abs(original - reversed_num)
        