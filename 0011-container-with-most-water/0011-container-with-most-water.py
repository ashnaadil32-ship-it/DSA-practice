class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        maxarea = 0

        while i < j :
            width = j - i
            heights = min(height[i],height[j])

            area = width * heights

            maxarea = max(area,maxarea)

            if height[i] < height[j]:
                i += 1
            else : 
                j -= 1
        return maxarea            
