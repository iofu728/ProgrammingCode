# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-25 21:44:54
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-25 22:30:29

"""
4. Median of Two Sorted Arrays Hard

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

## Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0

## Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
Accepted 616,039 Submissions 2,157,660
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        N, M = len(nums1), len(nums2)
        if N > M:
            N, M = M, N
            nums1, nums2 = nums2, nums1
        K = (N + M + 1) // 2
        left, right = 0, N
        while left < right:
            # print(left, right)
            t1 = left + (right - left) // 2
            t2 = K - t1
            if nums1[t1] > nums2[t2 - 1]:
                right = t1
            elif nums1[t1] == nums2[t2 - 1]:
                left = t1 + 1
                break
            else:
                left = t1 + 1
        t1 = left
        t2 = K - t1
        c1 = max(
            nums1[t1 - 1] if t1 else float("-inf"),
            nums2[t2 - 1] if t2 else float("-inf"),
        )
        if (N + M) % 2 == 1:
            return c1
        c2 = min(
            nums1[t1] if t1 < N else float("inf"), nums2[t2] if t2 < M else float("inf")
        )
        # print(t1, t2)
        return (c1 + c2) / 2

