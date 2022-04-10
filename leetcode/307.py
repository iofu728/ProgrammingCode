# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-04-04 12:01:59
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-04-04 12:02:34

"""
307. Range Sum Query - Mutable
Medium

2667

143

Add to List

Share
Given an integer array nums, handle multiple queries of the following types:

Update the value of an element in nums.
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
void update(int index, int val) Updates the value of nums[index] to be val.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

Example 1:

Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]

Explanation
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
 

Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
0 <= index < nums.length
-100 <= val <= 100
0 <= left <= right < nums.length
At most 3 * 104 calls will be made to update and sumRange.
Accepted
178,651
Submissions
462,502
"""
class SegmentTree:
    def __init__(self, nums: list):
        N = len(nums)
        self.N = N
        self.tree = [0] * N + nums
        for ii in range(N - 1, 0, -1):
            self.tree[ii] = self.tree[2 * ii] + self.tree[2 * ii + 1]

    def update(self, idx: int, val: int):
        idx += self.N
        gap = val - self.tree[idx]
        while idx:
            self.tree[idx] += gap
            idx //= 2
    
    def sum_range(self, left: int, right: int):
        l, r = left + self.N, right + self.N
        res = 0
        while l <= r:
            if l % 2 == 1:
                res += self.tree[l]
                l += 1
            if r % 2 == 0:
                res += self.tree[r]
                r -= 1
            l, r = l // 2, r // 2
        return res

class NumArray:
    def __init__(self, nums: List[int]):
        self.st = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        return self.st.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.st.sum_range(left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)