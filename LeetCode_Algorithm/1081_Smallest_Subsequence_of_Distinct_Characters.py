"""
LeetCode #1081: Smallest Subsequence of Distinct Characters
Difficulty: Medium
Date: 2026-06-01

[Complexity Analysis]
- Time Complexity: O(N)
  -> We traverse the string `s` twice: once to count frequencies and once to build the stack.
  -> Each character is pushed and popped from the stack at most once.
  -> Therefore, the overall time complexity scales linearly with the length of the string.

- Space Complexity: O(1)
  -> The `appear` and `seen` arrays have a fixed size of 26.
  -> The `stack` can hold at most 26 unique characters.
  -> Since the auxiliary space is bounded by the alphabet size, it remains constant.

[AI Mentor Feedback]
- Excellent implementation of the monotonic stack pattern to solve the smallest lexicographical sequence problem.
- Using a fixed-size array (`seen`) for O(1) lookups effectively avoids redundant stack operations and duplicate elements.
- The lookahead strategy using the `appear` frequency array correctly ensures that required characters are not permanently discarded.
- Using `ord()` arithmetic instead of high-overhead hash structures keeps the implementation highly cache-friendly.
- A minor improvement: `ans = "".join(stack)` can replace the string concatenation loop to build the final result more efficiently.

[Useful Technical English]
- "This approach utilizes a monotonic stack alongside frequency tracking to achieve linear time complexity."
- "The algorithm dynamically maintains the smallest lexicographical order by checking remaining character counts before popping."
- "Fixed-size status arrays guarantee constant auxiliary space usage regardless of the input string length."
"""
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        appear = [0]*26
        stack = []
        seen = [0]*26
        for i in s:
            appear[ord(i) - ord('a')] += 1

        for i in s:
            appear[ord(i) - ord('a')] -= 1
            if seen[ord(i) - ord('a')] == 1:
                continue

            while stack and i < stack[-1]:
                if appear[ord(stack[-1]) - ord('a')] > 0:
                    seen[ord(stack.pop()) - ord('a')] = 0
                else:
                    break
            stack.append(i)
            seen[ord(i) - ord('a')] = 1

        ans = ""
        for i in stack:
            ans = ans + i

        return ans
