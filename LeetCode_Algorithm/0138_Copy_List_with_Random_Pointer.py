"""
LeetCode #138: Copy List with Random Pointer
Difficulty: Medium
Date: 2026-05-29

[Complexity Analysis]
- Time Complexity: O(N)
  -> Let:
        N = number of nodes in the linked list
  -> The first traversal creates copied nodes and stores mappings.
  -> The second traversal reconstructs `next` and `random` relationships.
  -> Each node is processed a constant number of times.
  -> Therefore, the total complexity is linear.

- Space Complexity: O(N)
  -> A hashmap stores:
        original node -> copied node
  -> One copied node is created per original node.
  -> Thus, additional memory usage scales linearly with the list size.

[AI Mentor Feedback]
- Excellent use of hashmap-based node correspondence tracking.
- The solution correctly separates:
    1. Node allocation phase
    2. Pointer reconstruction phase
- Using original node objects directly as dictionary keys is an important Python-specific optimization.
- The implementation cleanly preserves arbitrary `random` graph connections.
- Explicit `None` handling prevents invalid hashmap access and edge-case failures.
- This is the canonical O(N) deep-copy strategy for graph-like linked structures.

[Useful Technical English]
- "The hashmap maintains a one-to-one correspondence between original and copied nodes."
- "The solution reconstructs pointer relationships in a second traversal."
- "Random pointers transform the linked list into a graph-like structure."
- "Deep copy requires allocating entirely new node objects."
- "The algorithm preserves structural equivalence without sharing memory references."
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        h = {}
        curr_node = head
        while curr_node != None:
            h[curr_node] = Node(curr_node.val)
            curr_node = curr_node.next
        curr_node = head
        while curr_node != None:
            h[curr_node].next = h[curr_node.next] if curr_node.next else None
            h[curr_node].random = h[curr_node.random] if curr_node.random else None
            curr_node = curr_node.next
        
        return h[head]