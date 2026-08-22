class Solution:
    def checkDivisibility(self, nums: int) -> bool:
        digit_sum = 0
        product = 1
        original = nums
        while nums > 0:
            last_digit = nums % 10
            nums = nums // 10
            digit_sum += last_digit 
            product *= last_digit

        if original % (digit_sum + product) == 0:
            return True 
        else:
            return False   
           