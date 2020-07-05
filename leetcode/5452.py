# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-05 10:30:21
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-05 10:32:37


"""
5452. 判断能否形成等差数列 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你一个数字数组 arr 。

如果一个数列中，任意相邻两项的差总等于同一个常数，那么这个数列就称为 等差数列 。

如果可以重新排列数组形成等差数列，请返回 true ；否则，返回 false 。

 

示例 1：

输入：arr = [3,5,1]
输出：true
解释：对数组重新排序得到 [1,3,5] 或者 [5,3,1] ，任意相邻两项的差分别为 2 或 -2 ，可以形成等差数列。
示例 2：

输入：arr = [1,2,4]
输出：false
解释：无法通过重新排序得到等差数列。
 

提示：

2 <= arr.length <= 1000
-10^6 <= arr[i] <= 10^6
"""


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        delta = set([arr[ii] - arr[ii - 1] for ii in range(1, len(arr))])
        return len(delta) in [1, 0]

