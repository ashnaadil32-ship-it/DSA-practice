class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        # Sort using a tuple key: (count of 1 bits, the number itself)
        arr.sort(key=lambda x: (x.bit_count(), x))
        return arr