class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        ans = []
        
        # Iterate through each string's index
        for i in range(len(nums)):
            # Look at the character at the diagonal position: nums[i][i]
            # Flip '0' to '1' and '1' to '0'
            if nums[i][i] == '0':
                ans.append('1')
            else:
                ans.append('0')
                
        return "".join(ans)