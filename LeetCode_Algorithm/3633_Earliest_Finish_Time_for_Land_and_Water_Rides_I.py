"""
LeetCode #3633: Earliest Finish Time for Land and Water Rides I
Difficulty: Easy
Date: 2026-06-02

[Complexity Analysis]
- Time Complexity: O(N + M)
  -> The algorithm independently iterates through the land ride lists of length N and the water ride lists of length M.
  -> Since it processes each element a constant number of times, the time complexity scales linearly with the input size.
- Space Complexity: O(1)
  -> The solution allocates a fixed number of scalar variables (`temp`, `ans1`, `ans2`) regardless of the input array sizes.
  -> Auxiliary space complexity remains constant as memory usage does not scale with N or M.

[AI Mentor Feedback]
- Great logical approach in evaluating both execution sequences (Land-to-Water and Water-to-Land) to safely ensure optimality.
- Replacing manual conditional ternary expressions with the built-in `min()` and `max()` functions will significantly enhance code readability and reduce cognitive load.
- Avoid hard-coding magic numbers like `10000` for initial minimum tracking, as this introduces potential logical failures if input values exceed this threshold. Utilizing `float('inf')` guarantees algorithmic robustness.
- Leveraging Python's native `zip()` function provides a more idiomatic approach to simultaneously traverse parallel arrays (`StartTime` and `Duration`) without index manipulation.

[Useful Technical English]
- "The solution evaluates both scheduling order scenarios to minimize the total elapsed time."
- "Replacing manual conditional assignments with built-in functions improves code legibility and maintainability."
- "Using float('inf') instead of hard-coded constants mitigates potential overflow or boundary logic errors."
- "The algorithm achieves linear time complexity with constant auxiliary space by avoiding dynamic memory allocation."
"""
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        # Case 1: Land Ride First -> Water Ride Second
        temp = 10000
        for i in range(len(landStartTime)):
            if temp > landDuration[i] + landStartTime[i]:
                temp =  landDuration[i] + landStartTime[i]
                
        ans1 = 10000
        for i in range(len(waterStartTime)):
            if temp >= waterStartTime[i]:
                ans1 = temp + waterDuration[i] if ans1 > temp + waterDuration[i] else ans1
            else:
                ans1 = waterStartTime[i] + waterDuration[i] if ans1 > waterStartTime[i] + waterDuration[i] else ans1
                
        # Case 2: Water Ride First -> Land Ride Second
        temp = 10000
        for i in range(len(waterStartTime)):
            if temp > waterDuration[i] + waterStartTime[i]:
                temp =  waterDuration[i] + waterStartTime[i]
                
        ans2 = 10000
        for i in range(len(landStartTime)):
            if temp >= landStartTime[i]:
                ans2 = temp + landDuration[i] if ans2 > temp + landDuration[i] else ans2
            else:
                ans2 = landStartTime[i] + landDuration[i] if ans2 > landStartTime[i] + landDuration[i] else ans2
                
        return ans1 if ans1 < ans2 else ans2

# ==============================================================================
# [AI Mentor Recommended Refactored Version]
# ==============================================================================
#     def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
#         # Use float('inf') to prevent out-of-bounds errors and zip() for idiomatic loop iteration
#         best_land_finish = min(s + d for s, d in zip(landStartTime, landDuration))
#         best_water_finish = min(s + d for s, d in zip(waterStartTime, waterDuration))
#         
#         # Streamline conditional state transitions using min() and max()
#         ans1, ans2 = float('inf'), float('inf')
#         
#         for s, d in zip(waterStartTime, waterDuration):
#             ans1 = min(ans1, max(best_land_finish, s) + d)
#             
#         for s, d in zip(landStartTime, landDuration):
#             ans2 = min(ans2, max(best_water_finish, s) + d)
#             
#         return min(ans1, ans2)
