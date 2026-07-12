import heapq

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
        # Min-heap stores: (next_available_time, worker_base_time, current_multiplier)
        # Next available time = current total worker time + (worker_base_time * current_multiplier)
        heap = []
        for time in workerTimes:
            heapq.heappush(heap, (time, time, 1))
            
        total_time = 0
        
        # Reduce the mountain height unit by unit
        for _ in range(mountainHeight):
            next_time, base_time, multiplier = heapq.heappop(heap)
            total_time = max(total_time, next_time)
            
            # Prepare the next job parameters for this worker
            next_multiplier = multiplier + 1
            next_job_cost = base_time * next_multiplier
            
            heapq.heappush(heap, (next_time + next_job_cost, base_time, next_multiplier))
            
        return total_time