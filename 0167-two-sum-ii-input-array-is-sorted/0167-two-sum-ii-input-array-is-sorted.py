class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left < right:
            current_sum = nums[left] + nums[right]

            if target == current_sum:
               return [left + 1, right + 1]
            elif current_sum > target :
                 right -=1
            else:
                left += 1     