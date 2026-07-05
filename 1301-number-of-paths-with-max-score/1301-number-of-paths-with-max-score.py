from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)
        
        dpScore = [[-1] * n for _ in range(n)]
        dpWays = [[0] * n for _ in range(n)]

        dpScore[n - 1][n - 1] = 0
        dpWays[n - 1][n - 1] = 1

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == 'X' or (i == n - 1 and j == n - 1):
                    continue

                bestScore = -1
                ways = 0

                for ni, nj in [(i + 1, j), (i, j + 1), (i + 1, j + 1)]:
                    if ni < n and nj < n and dpScore[ni][nj] != -1:
                        if dpScore[ni][nj] > bestScore:
                            bestScore = dpScore[ni][nj]
                            ways = dpWays[ni][nj]
                        elif dpScore[ni][nj] == bestScore:
                            ways = (ways + dpWays[ni][nj]) % MOD

                if bestScore == -1:
                    continue

                value = 0
                if board[i][j].isdigit():
                    value = int(board[i][j])

                dpScore[i][j] = bestScore + value
                dpWays[i][j] = ways % MOD

        if dpScore[0][0] == -1:
            return [0, 0]

        return [dpScore[0][0], dpWays[0][0]]