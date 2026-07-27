class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = float("-inf")
        second_largest = float("-inf")
        
        for num in nums:
            if num > largest :
                second_largest = largest
                largest = num
            elif num > second_largest :
                second_largest = num
            

            product = (largest - 1) * (second_largest - 1)
            
        return product   

        