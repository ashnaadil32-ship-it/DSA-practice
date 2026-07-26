class Solution:
    def majorityElement(self,nums : list[int]) -> int:
        count = 0
        candidate = None
        for current_element in nums:
            if count == 0:
                candidate = current_element 
                count += 1
            else:
                if current_element != candidate:
                    count -= 1
                else:
                    count += 1
        return candidate            