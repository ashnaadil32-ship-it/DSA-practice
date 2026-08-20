class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      freq = {}
      for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
        if freq[num] >= 2:
            return True   

      return False        

# Time Complexity  → O(n)
# Space Complexity → O(n)            
# ⭐ Important lesson

# return False ko loop ke bahar rakho.

# Because:

# True milte hi immediately return kar sakte ho, 
# but False tabhi return karna hai jab poori list check ho chuki ho.


