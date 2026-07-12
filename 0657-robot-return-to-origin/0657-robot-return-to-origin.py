class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # The robot returns to the origin if and only if:
        # 1. Number of Up moves == Number of Down moves
        # 2. Number of Right moves == Number of Left moves
        return moves.count('U') == moves.count('D') and moves.count('R') == moves.count('L')