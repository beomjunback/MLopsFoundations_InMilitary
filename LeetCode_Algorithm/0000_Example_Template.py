"""
LeetCode #0001: Two Sum
Difficulty: Easy
Date: 2026-05-26

[Complexity Analysis]
- Time Complexity: O(N) -> We traverse the list containing N elements only once.
- Space Complexity: O(N) -> The extra space required depends on the number of items stored in the hash table.

[AI Mentor Feedback]
- Dict lookup in Python takes O(1) on average. This optimizes the brute-force O(N^2) approach to O(N).
- Good practice to handle edge cases where no solution exists.

[Useful Technical English]
- "This approach leverages a hash map to achieve a linear time complexity."
"""

def twoSum(nums, target):
    hash_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_map:
            return [hash_map[complement], i]
        hash_map[num] = i
    return []