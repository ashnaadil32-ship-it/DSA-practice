class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for x in nums:
            if x not in seen:
                seen.add(x)
            else:
                return True
        return False        