# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-06 10:59:59
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-06 11:10:26

"""
5509. 避免重复字母的最小删除成本 显示英文描述 
通过的用户数318
尝试过的用户数378
用户总通过次数318
用户总提交次数470
题目难度Medium
给你一个字符串 s 和一个整数数组 cost ，其中 cost[i] 是从 s 中删除字符 i 的代价。

返回使字符串任意相邻两个字母不相同的最小删除成本。

请注意，删除一个字符后，删除其他字符的成本不会改变。

 

示例 1：

输入：s = "abaac", cost = [1,2,3,4,5]
输出：3
解释：删除字母 "a" 的成本为 3，然后得到 "abac"（字符串中相邻两个字母不相同）。
示例 2：

输入：s = "abc", cost = [1,2,3]
输出：0
解释：无需删除任何字母，因为字符串中不存在相邻两个字母相同的情况。
示例 3：

输入：s = "aabaa", cost = [1,2,3,4,1]
输出：2
解释：删除第一个和最后一个字母，得到字符串 ("aba") 。
 

提示：

s.length == cost.length
1 <= s.length, cost.length <= 10^5
1 <= cost[i] <= 10^4
s 中只含有小写英文字母
"""


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        N = len(s)
        b, e, pre = [], [], s[0]
        for ii in range(1, N):
            if s[ii] == pre:
                if len(e) and e[-1] == ii - 1:
                    e[-1] += 1
                else:
                    e.append(ii)
                    b.append(ii - 1)
            pre = s[ii]
        res = 0
        for ii, jj in zip(b, e):
            total = [cost[kk] for kk in range(ii, jj + 1)]
            res += sum(total) - max(total)
        return res
