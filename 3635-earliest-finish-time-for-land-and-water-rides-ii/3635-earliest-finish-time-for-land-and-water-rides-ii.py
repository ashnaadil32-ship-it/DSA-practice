class Solution:
    def earliestFinishTime(self, landStartTime: List[int],
                           landDuration: List[int],
                           waterStartTime: List[int],
                           waterDuration: List[int]) -> int:

        def calc(start1, duration1, start2, duration2):
            # Earliest finish of first ride
            min_end = min(
                start + duration
                for start, duration in zip(start1, duration1)
            )

            # Try every possible second ride
            return min(
                max(start, min_end) + duration
                for start, duration in zip(start2, duration2)
            )

        # Land -> Water
        land_water = calc(
            landStartTime, landDuration,
            waterStartTime, waterDuration
        )

        # Water -> Land
        water_land = calc(
            waterStartTime, waterDuration,
            landStartTime, landDuration
        )

        return min(land_water, water_land)