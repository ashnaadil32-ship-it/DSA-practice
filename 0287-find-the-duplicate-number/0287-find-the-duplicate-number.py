#brute force approach 
"""class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
     for i in range(0,len(nums)):
        for j in range(i+1,len(nums)) :
            if nums[i] == nums[j]:
               return nums[i]
                  """

                  
#One-line memory trick:
#Value ko index banao → visited index ko negative karo → negative mila = duplicate.
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            v = abs(nums[i])

            if nums[v] < 0:
                ans = v
                break
            else:
                nums[v] *= -1

        for i in range(n):
            if nums[i] < 0:
                nums[i] *= -1

        return ans                         