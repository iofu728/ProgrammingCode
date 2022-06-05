"""
715. Range Module
Hard

970

79

Add to List

Share
A Range Module is a module that tracks ranges of numbers. Design a data structure to track the ranges represented as half-open intervals and query about them.

A half-open interval [left, right) denotes all the real numbers x where left <= x < right.

Implement the RangeModule class:

RangeModule() Initializes the object of the data structure.
void addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval [left, right) that are not already tracked.
boolean queryRange(int left, int right) Returns true if every real number in the interval [left, right) is currently being tracked, and false otherwise.
void removeRange(int left, int right) Stops tracking every real number currently being tracked in the half-open interval [left, right).
 

Example 1:

Input
["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
[[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
Output
[null, null, null, true, false, true]

Explanation
RangeModule rangeModule = new RangeModule();
rangeModule.addRange(10, 20);
rangeModule.removeRange(14, 16);
rangeModule.queryRange(10, 14); // return True,(Every number in [10, 14) is being tracked)
rangeModule.queryRange(13, 15); // return False,(Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
rangeModule.queryRange(16, 17); // return True, (The number 16 in [16, 17) is still being tracked, despite the remove operation)
 

Constraints:

1 <= left < right <= 109
At most 104 calls will be made to addRange, queryRange, and removeRange.
Accepted
45,233
Submissions
103,280
"""
class Node:
    def __init__(self,l, r, track=False, lazy=None, lc=None, rc=None):
        self.track = track  # 表示当前区间所有元素是否被追踪
        self.lazy = lazy  # 表示当前区间的所有子区间应该更新的追踪状态，None表示子区间无需更新
        self.lc = lc
        self.rc = rc
        self.l = l
        self.r = r
        self.mid = (l + r) >> 1

class RangeModule:

    def __init__(self):
        self.tree = Node(0, int(1e9))

    def merge(self, node):
        node.track = bool(node.lc and node.lc.track and node.rc and node.rc.track)

    def pushdown(self, node):
        if not node.lc:
            node.lc = Node(node.l, node.mid)
        if not node.rc:
            node.rc = Node(node.mid+1, node.r)
        if node.lazy is not None:
            node.lc.track = node.lc.lazy = node.rc.track = node.rc.lazy = node.lazy
            node.lazy = None

    def _updateRange(self, tl, tr, node, val):  # tl,tr表示目标区间，l,r表示当前结点对应区间
        if tl <= node.l and node.r <= tr:
            node.track = node.lazy = val
            return
        
        self.pushdown(node) #如果到这里，一定有左右儿子
        
        if tl <= node.mid:
            self._updateRange(tl, tr, node.lc, val)
        if tr > node.mid:
            self._updateRange(tl, tr, node.rc, val)
        self.merge(node)

    def addRange(self, left: int, right: int) -> None:
        self._updateRange(left, right - 1, self.tree, True)

    def _queryRange(self, tl, tr, node):
        if tl <= node.l and node.r <= tr:
            return node.track

        self.pushdown(node)
        if tl > node.mid:
            return self._queryRange(tl, tr, node.rc)
        if tr <= node.mid:
            return self._queryRange(tl, tr, node.lc)
        else:
            return self._queryRange(tl, tr, node.lc) and self._queryRange(tl, tr, node.rc)

    def queryRange(self, left: int, right: int) -> bool:
        return self._queryRange(left, right - 1, self.tree)

    def removeRange(self, left: int, right: int) -> None:
        self._updateRange(left, right - 1, self.tree, False)

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)