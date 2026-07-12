class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        # Check if mat matches target after 0, 1, 2, or 3 rotations of 90 degrees
        for _ in range(4):
            if mat == target:
                return True
            # Rotate mat by 90 degrees clockwise in-place
            mat = [list(x) for x in zip(*mat[::-1])]
            
        return False