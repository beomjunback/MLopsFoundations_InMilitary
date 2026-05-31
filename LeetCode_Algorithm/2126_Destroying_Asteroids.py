"""
LeetCode #2126: Destroying Asteroids
Difficulty: Medium
Date: 2026-05-31

[Complexity Analysis]
- Time Complexity: O(N log N)
  -> Sorting the `asteroids` array takes O(N log N) time, where N is the number of asteroids.
  -> The subsequent linear scan takes O(N) time to iterate through the sorted list.
  -> Therefore, the sorting step dominates the overall time complexity.

- Space Complexity: O(1) to O(N)
  -> The space complexity depends entirely on the sorting algorithm implementation in Python (Timsort).
  -> Timsort requires O(N) auxiliary space in the worst case, but no additional user-defined data structures are used.

[AI Mentor Feedback]
- Great intuitive approach! A greedy strategy works perfectly here because destroying the smallest possible asteroid first maximizes the `mass` for subsequent challenges.
- Early exit logic (`if i > mass: return False`) is well-implemented, preventing unnecessary iterations once a failure condition is met.
- **Critical Edge Case Warning:** In Python, integers have arbitrary precision, so overflow is not an issue. However, in strongly-typed languages like C++ or Java, accumulating `mass` can easily exceed the 32-bit signed integer limit ($2 \times 10^31 - 1$). It is good practice to note that `mass` should be treated as a 64-bit integer (`long long` or `long`) in those environments.
- The use of meaningful variable names like `mass` and `asteroids` aligns well with clean coding standards.

[Useful Technical English]
- "A greedy approach is optimal here because destroying smaller asteroids first maximizes the accumulation of mass."
- "The sorting step dominates the overall runtime, yielding a time complexity of O(N log N)."
- "Early termination prevents redundant operations once the current mass is insufficient to destroy the next asteroid."
"""
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for i in asteroids:
            if i > mass:
                return False
            else:
                mass += i
        
        return True