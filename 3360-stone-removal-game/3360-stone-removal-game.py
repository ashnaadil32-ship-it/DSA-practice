
class Solution:
    def canAliceWin(self, n: int) -> bool:
        move = 10
        count = 0

        while n >= move:
            n -= move
            move -= 1
            count += 1

        return count % 2 == 1
