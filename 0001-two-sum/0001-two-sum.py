class Solution:
    def twoSum(self,nums:list,target:int)-> list[int]:
       seen = {}

       for i in range(len(nums)):
           rem = target - nums[i]

           if rem in seen:
              return [i,seen[rem]]  

           seen[nums[i]] = i        