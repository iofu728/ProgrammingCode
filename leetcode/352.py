# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-10-09 22:10:06
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-10-09 22:10:36

"""
352. Data Stream as Disjoint Intervals
Hard

532

128

Add to List

Share
Given a data stream input of non-negative integers a1, a2, ..., an, summarize the numbers seen so far as a list of disjoint intervals.

Implement the SummaryRanges class:

SummaryRanges() Initializes the object with an empty stream.
void addNum(int val) Adds the integer val to the stream.
int[][] getIntervals() Returns a summary of the integers in the stream currently as a list of disjoint intervals [starti, endi].
 

Example 1:

Input
["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
[[], [1], [], [3], [], [7], [], [2], [], [6], []]
Output
[null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]

Explanation
SummaryRanges summaryRanges = new SummaryRanges();
summaryRanges.addNum(1);      // arr = [1]
summaryRanges.getIntervals(); // return [[1, 1]]
summaryRanges.addNum(3);      // arr = [1, 3]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3]]
summaryRanges.addNum(7);      // arr = [1, 3, 7]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]]
summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
summaryRanges.getIntervals(); // return [[1, 3], [7, 7]]
summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]
 

Constraints:

0 <= val <= 104
At most 3 * 104 calls will be made to addNum and getIntervals.
 

Follow up: What if there are lots of merges and the number of disjoint intervals is small compared to the size of the data stream?

Accepted 45,939 Submissions 92,580
"""
from sortedcontainers import SortedDict


class SummaryRanges:
    def __init__(self):
        self.nums = SortedDict()

    def addNum(self, val: int) -> None:
        nums = self.nums
        keys = nums.keys()
        values = nums.values()

        idx1 = nums.bisect_right(val)
        idx0 = len(nums) if idx1 == 0 else (idx1 - 1)

        if idx0 != len(nums) and keys[idx0] <= val <= values[idx0]:
            return
        left_a = (idx0 != len(nums)) and values[idx0] + 1 == val
        right_a = (idx1 != len(nums)) and keys[idx1] - 1 == val
        if left_a and right_a:
            left, right = keys[idx0], values[idx1]
            nums.popitem(idx1)
            nums.popitem(idx0)
            nums[left] = right
        elif left_a:
            nums[keys[idx0]] += 1
        elif right_a:
            right = values[idx1]
            nums.popitem(idx1)
            nums[val] = right
        else:
            nums[val] = val

    def getIntervals(self) -> List[List[int]]:
        return list(self.nums.items())


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()