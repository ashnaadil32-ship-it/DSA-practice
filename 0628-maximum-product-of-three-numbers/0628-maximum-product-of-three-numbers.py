class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        a = sorted(nums)
        product_1 = a[-1] * a[-2] * a[-3]
        product_2 = a[-1] * a[0] * a[1]
        return max(product_1,product_2)
        