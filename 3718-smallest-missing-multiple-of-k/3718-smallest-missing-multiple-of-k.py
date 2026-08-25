class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s = set(nums)

        i = 1

        while True:
            multiple = k * i

            if multiple not in s:
                return multiple

            i += 1