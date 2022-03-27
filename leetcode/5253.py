# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-03-27 11:13:23
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-03-27 11:13:41

"""
5253. 找到指定长度的回文数 显示英文描述 
通过的用户数0
尝试过的用户数1
用户总通过次数0
用户总提交次数1
题目难度Medium
给你一个整数数组 queries 和一个 正 整数 intLength ，请你返回一个数组 answer ，其中 answer[i] 是长度为 intLength 的 正回文数 中第 queries[i] 小的数字，如果不存在这样的回文数，则为 -1 。

回文数 指的是从前往后和从后往前读一模一样的数字。回文数不能有前导 0 。

 

示例 1：

输入：queries = [1,2,3,4,5,90], intLength = 3
输出：[101,111,121,131,141,999]
解释：
长度为 3 的最小回文数依次是：
101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 201, ...
第 90 个长度为 3 的回文数是 999 。
示例 2：

输入：queries = [2,4,6], intLength = 4
输出：[1111,1331,1551]
解释：
长度为 4 的前 6 个回文数是：
1001, 1111, 1221, 1331, 1441 和 1551 。
 

提示：

1 <= queries.length <= 5 * 104
1 <= queries[i] <= 109
1 <= intLength <= 15
"""
class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        @lru_cache(None)
        def get_k(n):
            if n > upper:
                return -1
            x = base + (n - 1)
            if is_a:
                return int(str(x) + str(x)[::-1])
            return int(str(x) + str(x)[::-1][1:])
        N = (intLength - 1) // 2 + 1
        is_a = intLength >> 1 << 1 == intLength
        base = 10 ** (N - 1)
        upper = 10 ** (N) - base
        return [get_k(ii) for ii in queries]
        