"""
LeetCode #3121: Count the Number of Special Characters II
Difficulty: Medium
Date: 2026-05-27

[Complexity Analysis]
- Time Complexity: O(N)
  -> We traverse the input string once, and the final verification loop runs a fixed 26 iterations.
  -> Therefore, the overall complexity is linear with respect to the length of the string.

- Space Complexity: O(1)
  -> Two arrays of fixed size 26 are used regardless of input size.
  -> Since the memory usage does not scale with N, the auxiliary space complexity is constant.

[AI Mentor Feedback]
- Good use of fixed-size frequency/state arrays instead of hash maps. This is cache-friendly and memory-efficient.
- The state transition logic using `upp[i] = -1` effectively invalidates characters when lowercase appears after uppercase.
- Using `ord()` arithmetic avoids additional dictionary overhead and demonstrates understanding of ASCII indexing.
- A small optimization is possible by merging `upp` and `low` into a single state array to reduce memory usage and improve readability.
- Since the alphabet size is fixed to 26, the final validation loop is effectively O(1).

[Useful Technical English]
- "This solution achieves linear time complexity with constant auxiliary space."
- "The algorithm uses fixed-size state arrays to efficiently track character ordering constraints."
- "ASCII-based indexing minimizes hash lookup overhead and improves cache locality."
"""
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        upp = [0] * 26
        low = [0] * 26
        cnt = 0
        
        for i in word:
            if i.isupper():
                if upp[ord(i) - ord('A')] == 0:
                    upp[ord(i) - ord('A')] = 1
            else:
                if upp[ord(i) - ord('a')] == 1:
                    upp[ord(i) - ord('a')] = -1
                low[ord(i) - ord('a')] = 1

        for i in range(26):
            if upp[i] == 1 and low[i] == 1:
                cnt += 1
        
        return cnt