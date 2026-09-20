class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int],
                           waterStartTime: List[int], waterDuration: List[int]) -> int:

        ans = float('inf')

        # Land → Water
        for i in range(len(landStartTime)):
            land_finish = landStartTime[i] + landDuration[i]

            for j in range(len(waterStartTime)):
                water_start = max(land_finish, waterStartTime[j])
                finish = water_start + waterDuration[j]

                ans = min(ans, finish)

        # Water → Land
        for i in range(len(waterStartTime)):
            water_finish = waterStartTime[i] + waterDuration[i]

            for j in range(len(landStartTime)):
                land_start = max(water_finish, landStartTime[j])
                finish = land_start + landDuration[j]

                ans = min(ans, finish)

        return ans