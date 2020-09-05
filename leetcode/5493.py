# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-05 22:55:16
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-05 23:24:32

"""
5493. 删除最短的子数组使剩余数组有序 显示英文描述 
通过的用户数82
尝试过的用户数257
用户总通过次数83
用户总提交次数395
题目难度Medium
给你一个整数数组 arr ，请你删除一个子数组（可以为空），使得 arr 中剩下的元素是 非递减 的。

一个子数组指的是原数组中连续的一个子序列。

请你返回满足题目要求的最短子数组的长度。

 

示例 1：

输入：arr = [1,2,3,10,4,2,3,5]
输出：3
解释：我们需要删除的最短子数组是 [10,4,2] ，长度为 3 。剩余元素形成非递减数组 [1,2,3,3,5] 。
另一个正确的解为删除子数组 [3,10,4] 。
示例 2：

输入：arr = [5,4,3,2,1]
输出：4
解释：由于数组是严格递减的，我们只能保留一个元素。所以我们需要删除长度为 4 的子数组，要么删除 [5,4,3,2]，要么删除 [4,3,2,1]。
示例 3：

输入：arr = [1,2,3]
输出：0
解释：数组已经是非递减的了，我们不需要删除任何元素。
示例 4：

输入：arr = [1]
输出：0
 

提示：

1 <= arr.length <= 10^5
0 <= arr[i] <= 10^9
"""


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        N = len(arr)
        left, right = 0, N - 1
        while left + 1 < N and arr[left + 1] >= arr[left]:
            left += 1
        while right - 1 >= 0 and arr[right - 1] <= arr[right]:
            right -= 1
        res = min(N - 1, N - left - 1, right)
        l, r = left, right
        # print(l, r)
        if arr[l] <= arr[r]:
            return max(r - l - 1, 0)
        while r < N and arr[r] < arr[l]:
            r += 1
        while l >= 0 and r >= right:
            while r - 1 >= right and arr[l] <= arr[r - 1]:
                r -= 1
            res = min(res, max(r - l - 1, 0))
            # print(r, l, res)
            l -= 1
        return res

