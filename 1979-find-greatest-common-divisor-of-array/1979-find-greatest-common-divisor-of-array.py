class Solution:
    def findGCD(self, nums: List[int]) -> int:
         nums.sort()
         a = nums[0]
         b = nums[-1]
         if b % a == 0:
            return a
         while  a != 0:
            remainder = b % a
            b = a
            a = remainder
         return b  



        