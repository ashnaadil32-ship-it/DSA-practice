class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        # 1. Find all unique elements and sort them
        sorted_unique = sorted(list(set(arr)))
        
        # 2. Map each element to its 1-based rank
        rank_map = {num: rank + 1 for rank, num in enumerate(sorted_unique)}
        
        # 3. Replace each original element with its rank
        return [rank_map[num] for num in arr]