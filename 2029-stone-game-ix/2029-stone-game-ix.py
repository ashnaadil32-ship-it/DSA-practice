class Solution:
    def stoneGameIX(self, stones):
        count = [0, 0, 0]

        for stone in stones:
            count[stone % 3] += 1

        # count[0] = stones divisible by 3
        # count[1] = remainder 1
        # count[2] = remainder 2

        if count[0] % 2 == 0:
            return count[1] > 0 and count[2] > 0

        return abs(count[1] - count[2]) > 2