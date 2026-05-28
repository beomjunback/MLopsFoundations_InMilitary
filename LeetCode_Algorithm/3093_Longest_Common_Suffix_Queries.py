"""
LeetCode #3093: Longest Common Suffix Queries
Difficulty: Hard
Date: 2026-05-28

[Complexity Analysis]
- Time Complexity: O(N + Q)
  -> Let:
        N = total number of characters in wordsContainer
        Q = total number of characters in wordsQuery
  -> Trie construction processes every character once.
  -> Query traversal also processes each character once.
  -> Therefore, the overall complexity is linear with respect to the total input size.

- Space Complexity: O(N)
  -> Each character from wordsContainer may create one Trie node.
  -> Additional metadata (`best_idx`, `best_len`) is stored per node.
  -> Thus, memory usage scales linearly with the total container string length.

[AI Mentor Feedback]
- Excellent transformation of a suffix problem into a prefix Trie problem using reversed strings.
- Maintaining optimal candidate metadata at every Trie node eliminates unnecessary subtree traversal.
- The solution cleanly separates:
    1. Longest suffix matching via Trie depth
    2. Tie-breaking via node metadata
- Query processing is highly efficient because the stopping node already contains the final answer.
- The implementation achieves near-optimal complexity for this problem class.

[Useful Technical English]
- "The suffix matching problem is transformed into a prefix Trie problem by reversing strings."
- "Trie depth implicitly guarantees the longest common suffix."
- "Each Trie node stores the optimal candidate index for efficient query resolution."
- "The algorithm avoids expensive subtree searches through metadata propagation during insertion."
"""

class Node(object):
    def __init__(self,key, data = None):
        self.key = key
        self.children = {}
        self.best_idx = -1
        self.best_len = float('inf')

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self,string, idx, length):
        curr_node = self.head
        if length < curr_node.best_len:
            curr_node.best_len = length
            curr_node.best_idx = idx
        
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]

            if length < curr_node.best_len:
                curr_node.best_len = length
                curr_node.best_idx = idx

    def query(self,string):
        curr_node = self.head
        for char in string:
            if char not in curr_node.children:
                break
            curr_node = curr_node.children[char]
        return curr_node.best_idx


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        tr = Trie()
        ans = []
        for i in range(len(wordsContainer)):
            tr.insert(wordsContainer[i][::-1],i,len(wordsContainer[i]))
        
        for k in wordsQuery:
            ans.append(tr.query(k[::-1]))

        return ans