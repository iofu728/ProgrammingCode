# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-04-17 15:16:31
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-04-17 15:16:50

"""
1300. Sum of Mutated Array Closest to Target
Medium

736

89

Add to List

Share
Given an integer array arr and a target value target, return the integer value such that when we change all the integers larger than value in the given array to be equal to value, the sum of the array gets as close as possible (in absolute difference) to target.

In case of a tie, return the minimum such integer.

Notice that the answer is not neccesarilly a number from arr.

 

Example 1:

Input: arr = [4,9,3], target = 10
Output: 3
Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.
Example 2:

Input: arr = [2,3,5], target = 10
Output: 5
Example 3:

Input: arr = [60864,25176,27249,21296,20204], target = 56803
Output: 11361
 

Constraints:

1 <= arr.length <= 104
1 <= arr[i], target <= 105
Accepted
24,420
Submissions
57,295
"""
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        def get_sum(m):
            idx = bisect.bisect_left(arr, m)
            tmp = prefix[idx] + (N - idx) * m
            return tmp
        N = len(arr)
        arr = sorted(arr)
        prefix = [0]
        for ii in arr:
            prefix.append(prefix[-1] + ii)

        l, r = 0, arr[-1]
        while l < r:
            m = (l + r) // 2
            tmp = get_sum(m)
            if tmp <= target:
                l = m + 1
            else:
                r = m
        a, b = get_sum(l - 1), get_sum(l)
        return l - 1 if abs(a - target) <= abs(b - target) else l
