# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-07-31 13:06:45
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-07-31 13:06:59

"""
6133. 分组的最大数量 显示英文描述 
通过的用户数4
尝试过的用户数6
用户总通过次数4
用户总提交次数6
题目难度Medium
给你一个正整数数组 grades ，表示大学中一些学生的成绩。你打算将 所有 学生分为一些 有序 的非空分组，其中分组间的顺序满足以下全部条件：

第 i 个分组中的学生总成绩 小于 第 (i + 1) 个分组中的学生总成绩，对所有组均成立（除了最后一组）。
第 i 个分组中的学生总数 小于 第 (i + 1) 个分组中的学生总数，对所有组均成立（除了最后一组）。
返回可以形成的 最大 组数。

 

示例 1：

输入：grades = [10,6,12,7,3,5]
输出：3
解释：下面是形成 3 个分组的一种可行方法：
- 第 1 个分组的学生成绩为 grades = [12] ，总成绩：12 ，学生数：1
- 第 2 个分组的学生成绩为 grades = [6,7] ，总成绩：6 + 7 = 13 ，学生数：2
- 第 3 个分组的学生成绩为 grades = [10,3,5] ，总成绩：10 + 3 + 5 = 18 ，学生数：3 
可以证明无法形成超过 3 个分组。
示例 2：

输入：grades = [8,8]
输出：1
解释：只能形成 1 个分组，因为如果要形成 2 个分组的话，会导致每个分组中的学生数目相等。
 

提示：

1 <= grades.length <= 105
1 <= grades[i] <= 105
"""


class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        @lru_cache(None)
        def is_ok(x):
            return x * (x + 1) <= 2 * N

        N = len(grades)
        l, r = 1, N - 1
        while l < r:
            m = (l + r) // 2
            if m in [l, r]:
                if is_ok(r):
                    l = r = r
                else:
                    l = r = l
                continue
            if is_ok(m):
                l = m
            else:
                r = m - 1
        return l