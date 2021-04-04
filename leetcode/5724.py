# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-04-04 10:53:58
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-04-04 10:54:10

"""
5724. 绝对差值和 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你两个正整数数组 nums1 和 nums2 ，数组的长度都是 n 。

数组 nums1 和 nums2 的 绝对差值和 定义为所有 |nums1[i] - nums2[i]|（0 <= i < n）的 总和（下标从 0 开始）。

你可以选用 nums1 中的 任意一个 元素来替换 nums1 中的 至多 一个元素，以 最小化 绝对差值和。

在替换数组 nums1 中最多一个元素 之后 ，返回最小绝对差值和。因为答案可能很大，所以需要对 109 + 7 取余 后返回。

|x| 定义为：

如果 x >= 0 ，值为 x ，或者
如果 x <= 0 ，值为 -x
 

示例 1：

输入：nums1 = [1,7,5], nums2 = [2,3,5]
输出：3
解释：有两种可能的最优方案：
- 将第二个元素替换为第一个元素：[1,7,5] => [1,1,5] ，或者
- 将第二个元素替换为第三个元素：[1,7,5] => [1,5,5]
两种方案的绝对差值和都是 |1-2| + (|1-3| 或者 |5-3|) + |5-5| = 3
示例 2：

输入：nums1 = [2,4,6,8,10], nums2 = [2,4,6,8,10]
输出：0
解释：nums1 和 nums2 相等，所以不用替换元素。绝对差值和为 0
示例 3：

输入：nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4]
输出：20
解释：将第一个元素替换为第二个元素：[1,10,4,4,2,7] => [10,10,4,4,2,7]
绝对差值和为 |10-9| + |10-3| + |4-5| + |4-1| + |2-7| + |7-4| = 20
 

提示：

n == nums1.length
n == nums2.length
1 <= n <= 105
1 <= nums1[i], nums2[i] <= 105
"""
import bisect


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        max_diff, res = 0, 0
        nums1_sort = sorted(nums1)
        nums1_set = set(nums1)
        for ii, jj in zip(nums1, nums2):
            diff = abs(ii - jj)
            res += diff
            if jj in nums1_set:
                now = 0
            else:
                idx = bisect.bisect_left(nums1_sort, jj)
                data = []
                if idx:
                    data.append(abs(nums1_sort[idx - 1] - jj))
                if idx < N:
                    data.append(abs(nums1_sort[idx] - jj))
                now = min(data)
            diff -= now
            if diff > max_diff:
                max_diff = diff
        return (res - max_diff) % (10 ** 9 + 7)