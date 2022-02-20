# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-02-19 13:25:47
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-02-19 13:26:17

"""
1675. Minimize Deviation in Array
Hard

731

37

Add to List

Share
You are given an array nums of n positive integers.

You can perform two types of operations on any element of the array any number of times:

If the element is even, divide it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
If the element is odd, multiply it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].
The deviation of the array is the maximum difference between any two elements in the array.

Return the minimum deviation the array can have after performing some number of operations.

 

Example 1:

Input: nums = [1,2,3,4]
Output: 1
Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2], then the deviation will be 3 - 2 = 1.
Example 2:

Input: nums = [4,1,5,20,3]
Output: 3
Explanation: You can transform the array after two operations to [4,2,5,5,3], then the deviation will be 5 - 2 = 3.
Example 3:

Input: nums = [2,10,8]
Output: 3
 

Constraints:

n == nums.length
2 <= n <= 105
1 <= nums[i] <= 109
Accepted
21,844
Submissions
43,868
"""


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        q = sorted([-ii if ii >> 1 << 1 == ii else -2 * ii for ii in nums])
        min_v = -q[-1]
        res = q[-1] - q[0]
        while True:
            top = -heapq.heappop(q)
            res = min(res, top - min_v)
            if top >> 1 << 1 != top:
                break
            top //= 2
            min_v = min(top, min_v)
            heapq.heappush(q, -top)
        return res
