class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # If "01" exists, it means a new segment of 1s started after a 0
        return "01" not in s   