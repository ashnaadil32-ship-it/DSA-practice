class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        # Helper function to calculate the product of digits of a number
        def get_digit_product(num: int) -> int:
            product = 1
            while num > 0:
                product *= num % 10
                num //= 10
            return product

        # Check numbers starting from n upwards
        for current in range(n, n + 10):
            if get_digit_product(current) % t == 0:
                return current    