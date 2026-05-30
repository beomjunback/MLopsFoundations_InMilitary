"""
LeetCode #3161: Block Placement Queries
Difficulty: Hard
Date: 2026-05-30

[Complexity Analysis]
- Time Complexity: O(Q * log(M))
  -> For each type 1 query, 'SortedList' takes O(log Q) to insert, and the Segment Tree updates at most two points in O(log M) time, where M is max_x.
  -> For each type 2 query, 'SortedList' takes O(log Q) for binary search, and the Segment Tree queries the range maximum in O(log M) time.
  -> Thus, the total time complexity scales efficiently as O(Q * log(M)), passing well within the execution time limit.

- Space Complexity: O(M + Q)
  -> The Segment Tree array requires O(4 * M) space to handle range maximum updates across the coordinate range.
  -> The 'SortedList' stores coordinates of up to Q dynamic obstacles, leading to O(Q) auxiliary space.
  -> Hence, the overall space complexity is O(M + Q), which fits securely within memory constraints.

[AI Mentor Feedback]
- Brilliant translation of a geometry/interval problem into a point-update range-maximum Segment Tree problem by indexing "coordinate position to left-gap distance".
- Excellent edge-case handling by initializing the SortedList with, effectively standardizing the boundary gap calculation without complex if-else branches.
- The separation of the encapsulated interior maximum gap (`max_inner_gap`) and the trailing remainder gap (`last_gap`) is highly precise and mathematically sound.
- A minor runtime optimization can be achieved by tracking `max_x` dynamically up to 50,000 as per constraints, avoiding redundant tree sizing if query values are tiny.
- Overall, utilizing a point-update strategy instead of interval lazy propagation successfully minimized overhead and provided a clean, high-performance implementation.

[Useful Technical English]
- "This solution achieves efficient logarithmic time complexity per query using a dynamic Segment Tree."
- "The algorithm reformulates the block placement problem as a range maximum query over obstacle distances."
- "By maintaining obstacle coordinates in a sorted order, we isolate and verify the trailing remainder space in O(1) time."
"""
from sortedcontainers import SortedList

class SegmentTree:
    def __init__(self, size):
        self.tree = [0] * (4*size)

    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if start <= idx <= mid:
            self.update(node*2,start,mid,idx,val)
        else:
            self.update(node*2 + 1, mid+1,end, idx, val)
        self.tree[node] = max(self.tree[2*node], self.tree[2*node + 1])

    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start+end)//2
        temp1 = self.query(2*node,start,mid,l,r)
        temp2 = self.query(2*node+1,mid+1,end,l,r)
        return max(temp1,temp2)
    
class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        max_x = max([q[1] for q in queries]) + 1
        seg_tree = SegmentTree(max_x)
        obstacles = SortedList([0]) 
        results = []

        for q in queries:
            if q[0] == 1:
                x = q[1]
                obstacles.add(x)
                idx = obstacles.index(x)
                
                prev_val = obstacles[idx - 1]
                seg_tree.update(1, 0, max_x - 1, x, x - prev_val)
                if idx + 1 < len(obstacles):
                    next_val = obstacles[idx + 1]
                    seg_tree.update(1, 0, max_x - 1, next_val, next_val - x)
                    
            elif q[0] == 2:
                x, sz = q[1], q[2]
                idx = obstacles.bisect_right(x) - 1
                prev_x = obstacles[idx]
                max_inner_gap = seg_tree.query(1, 0, max_x - 1, 0, prev_x)
                last_gap = x - prev_x
                if max(max_inner_gap, last_gap) >= sz:
                    results.append(True)
                else:
                    results.append(False)
                    
        return results
