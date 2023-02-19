# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-02-19 12:53:51
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-02-19 12:54:37

"""
6362. 合并两个二维数组 - 求和法 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你两个 二维 整数数组 nums1 和 nums2.

nums1[i] = [idi, vali] 表示编号为 idi 的数字对应的值等于 vali 。
nums2[i] = [idi, vali] 表示编号为 idi 的数字对应的值等于 vali 。
每个数组都包含 互不相同 的 id ，并按 id 以 递增 顺序排列。

请你将两个数组合并为一个按 id 以递增顺序排列的数组，并符合下述条件：

只有在两个数组中至少出现过一次的 id 才能包含在结果数组内。
每个 id 在结果数组中 只能出现一次 ，并且其对应的值等于两个数组中该 id 所对应的值求和。如果某个数组中不存在该 id ，则认为其对应的值等于 0 。
返回结果数组。返回的数组需要按 id 以递增顺序排列。

 

示例 1：

输入：nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]
输出：[[1,6],[2,3],[3,2],[4,6]]
解释：结果数组中包含以下元素：
- id = 1 ，对应的值等于 2 + 4 = 6 。
- id = 2 ，对应的值等于 3 。
- id = 3 ，对应的值等于 2 。
- id = 4 ，对应的值等于5 + 1 = 6 。
示例 2：

输入：nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]
输出：[[1,3],[2,4],[3,6],[4,3],[5,5]]
解释：不存在共同 id ，在结果数组中只需要包含每个 id 和其对应的值。
 

提示：

1 <= nums1.length, nums2.length <= 200
nums1[i].length == nums2[j].length == 2
1 <= idi, vali <= 1000
数组中的 id 互不相同
数据均按 id 以严格递增顺序排列
"""


class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        d = defaultdict(int)
        for ii, jj in nums1 + nums2:
            d[ii] += jj
        return [[ii, d[ii]] for ii in sorted(d.keys())]
