# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-11-27 23:29:10
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-11-27 23:29:26

"""
5923. 从房屋收集雨水需要的最少水桶数 显示英文描述 
User Accepted:0
User Tried:0
Total Accepted:0
Total Submissions:0
Difficulty:Medium
给你一个下标从 0 开始的字符串 street 。street 中每个字符要么是表示房屋的 'H' ，要么是表示空位的 '.' 。

你可以在 空位 放置水桶，从相邻的房屋收集雨水。位置在 i - 1 或者 i + 1 的水桶可以收集位置为 i 处房屋的雨水。一个水桶如果相邻两个位置都有房屋，那么它可以收集 两个 房屋的雨水。

在确保 每个 房屋旁边都 至少 有一个水桶的前提下，请你返回需要的 最少 水桶数。如果无解请返回 -1 。

 

示例 1：

输入：street = "H..H"
输出：2
解释：
我们可以在下标为 1 和 2 处放水桶。
"H..H" -> "HBBH"（'B' 表示放置水桶）。
下标为 0 处的房屋右边有水桶，下标为 3 处的房屋左边有水桶。
所以每个房屋旁边都至少有一个水桶收集雨水。
示例 2：

输入：street = ".H.H."
输出：1
解释：
我们可以在下标为 2 处放置一个水桶。
".H.H." -> ".HBH."（'B' 表示放置水桶）。
下标为 1 处的房屋右边有水桶，下标为 3 处的房屋左边有水桶。
所以每个房屋旁边都至少有一个水桶收集雨水。
示例 3：

输入：street = ".HHH."
输出：-1
解释：
没有空位可以放置水桶收集下标为 2 处的雨水。
所以没有办法收集所有房屋的雨水。
示例 4：

输入：street = "H"
输出：-1
解释：
没有空位放置水桶。
所以没有办法收集所有房屋的雨水。
示例 5：

输入：street = "."
输出：0
解释：
没有房屋需要收集雨水。
所以需要 0 个水桶。
 

提示：

1 <= street.length <= 105
street[i] 要么是 'H' ，要么是 '.' 。
"""
class Solution:
    def minimumBuckets(self, street: str) -> int:
        def is_ok(idx):
            return 0 <= idx < N and street[idx] == "."
        N = len(street)
        g = defaultdict(list)
        hs = defaultdict(list)
        have = set()
        res = 0
        for ii, jj in enumerate(street):
            if jj != "H":
                continue
            if not is_ok(ii - 1) and not is_ok(ii + 1):
                return -1
            if ii - 1 in have:
                continue
            if is_ok(ii + 1):
                have.add(ii + 1)
            elif is_ok(ii - 1):
                have.add(ii - 1)
            res += 1
        return res
            
        