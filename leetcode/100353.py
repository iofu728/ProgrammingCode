# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-09-08 12:58:50
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-09-08 12:58:59

"""
100353. 范围内整数的最大得分 显示英文描述 
通过的用户数915
尝试过的用户数1501
用户总通过次数957
用户总提交次数4104
题目难度Medium
给你一个整数数组 start 和一个整数 d，代表 n 个区间 [start[i], start[i] + d]。

你需要选择 n 个整数，其中第 i 个整数必须属于第 i 个区间。所选整数的 得分 定义为所选整数两两之间的 最小 绝对差。

返回所选整数的 最大可能得分 。

 

示例 1：

输入： start = [6,0,3], d = 2

输出： 4

解释：

可以选择整数 8, 0 和 4 获得最大可能得分，得分为 min(|8 - 0|, |8 - 4|, |0 - 4|)，等于 4。

示例 2：

输入： start = [2,6,13,13], d = 5

输出： 5

解释：

可以选择整数 2, 7, 13 和 18 获得最大可能得分，得分为 min(|2 - 7|, |2 - 13|, |2 - 18|, |7 - 13|, |7 - 18|, |13 - 18|)，等于 5。

 

提示：

2 <= start.length <= 105
0 <= start[i] <= 109
0 <= d <= 109
"""
class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        def is_ok(y):
            s = start[0]
            for ii in start[1:]:
                if s + y > ii + d:
                    return False
                s = max(s + y, ii)
            return True
        start = sorted(start)
        l, r = -1, start[-1] - start[0] + 1 + d
        while l < r:
            m = (l + r) // 2
            if is_ok(m):
                l = m + 1
            else:
                r = m
            # print(l, r)
        return l - 1