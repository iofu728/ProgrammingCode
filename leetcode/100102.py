# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-10-29 11:44:37
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-10-29 11:44:46

"""
100102. 数组的最小相等和 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你两个由正整数和 0 组成的数组 nums1 和 nums2 。

你必须将两个数组中的 所有 0 替换为 严格 正整数，并且满足两个数组中所有元素的和 相等 。

返回 最小 相等和 ，如果无法使两数组相等，则返回 -1 。

 

示例 1：

输入：nums1 = [3,2,0,1,0], nums2 = [6,5,0]
输出：12
解释：可以按下述方式替换数组中的 0 ：
- 用 2 和 4 替换 nums1 中的两个 0 。得到 nums1 = [3,2,2,1,4] 。
- 用 1 替换 nums2 中的一个 0 。得到 nums2 = [6,5,1] 。
两个数组的元素和相等，都等于 12 。可以证明这是可以获得的最小相等和。
示例 2：

输入：nums1 = [2,0,2,0], nums2 = [1,4]
输出：-1
解释：无法使两个数组的和相等。
 

提示：

1 <= nums1.length, nums2.length <= 105
0 <= nums1[i], nums2[i] <= 106

"""
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sa, sb = sum(nums1), sum(nums2)
        if sa > sb:
            sa, sb = sb, sa
            nums1, nums2 = nums2, nums1
        a, b = nums1.count(0), nums2.count(0)
        if sa == sb and a == 0 and b == 0:
            return sa
        # print(sa, sb, a, b)
        if sa == sb and a > b:
            a, b = b, a
        if a == 0 or (b == 0 and sa + a > sb + b and sa != sb):
            return -1
        return max(sb + b, sa + a)
        