# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-08 23:02:05
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-08 23:07:08

"""
5468. 第 k 个缺失的正整数 显示英文描述 
通过的用户数1708
尝试过的用户数1822
用户总通过次数1723
用户总提交次数3064
题目难度Easy
给你一个 严格升序排列 的正整数数组 arr 和一个整数 k 。

请你找到这个数组里第 k 个缺失的正整数。

 

示例 1：

输入：arr = [2,3,4,7,11], k = 5
输出：9
解释：缺失的正整数包括 [1,5,6,8,9,10,12,13,...] 。第 5 个缺失的正整数为 9 。
示例 2：

输入：arr = [1,2,3,4], k = 2
输出：6
解释：缺失的正整数包括 [5,6,7,...] 。第 2 个缺失的正整数为 6 。
 

提示：

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
对于所有 1 <= i < j <= arr.length 的 i 和 j 满足 arr[i] < arr[j] 
"""
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        res, idx = [], 1
        N = len(arr)
        while len(res) < k:
            if idx not in arr:
                res.append(idx)
            if idx > arr[-1]:
                break
            idx += 1
        res.extend(range(res[-1] + 1, k - len(res) + res[-1] + 1))
        return res[-1]

