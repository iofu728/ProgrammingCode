# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-03-10 14:07:26
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-03-10 14:07:38

"""
100251. 数组中的最短非公共子字符串 显示英文描述 
通过的用户数2
尝试过的用户数5
用户总通过次数2
用户总提交次数5
题目难度Medium
给你一个数组 arr ，数组中有 n 个 非空 字符串。

请你求出一个长度为 n 的字符串 answer ，满足：

answer[i] 是 arr[i] 最短 的子字符串，且它不是 arr 中其他任何字符串的子字符串。如果有多个这样的子字符串存在，answer[i] 应该是它们中字典序最小的一个。如果不存在这样的子字符串，answer[i] 为空字符串。
请你返回数组 answer 。

 

示例 1：

输入：arr = ["cab","ad","bad","c"]
输出：["ab","","ba",""]
解释：求解过程如下：
- 对于字符串 "cab" ，最短没有在其他字符串中出现过的子字符串是 "ca" 或者 "ab" ，我们选择字典序更小的子字符串，也就是 "ab" 。
- 对于字符串 "ad" ，不存在没有在其他字符串中出现过的子字符串。
- 对于字符串 "bad" ，最短没有在其他字符串中出现过的子字符串是 "ba" 。
- 对于字符串 "c" ，不存在没有在其他字符串中出现过的子字符串。
示例 2：

输入：arr = ["abc","bcd","abcd"]
输出：["","","abcd"]
解释：求解过程如下：
- 对于字符串 "abc" ，不存在没有在其他字符串中出现过的子字符串。
- 对于字符串 "bcd" ，不存在没有在其他字符串中出现过的子字符串。
- 对于字符串 "abcd" ，最短没有在其他字符串中出现过的子字符串是 "abcd" 。
 

提示：

n == arr.length
2 <= n <= 100
1 <= arr[i].length <= 20
arr[i] 只包含小写英文字母。
"""
class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        res = []
        N = len(arr)
        for idx, x in enumerate(arr):
            n = len(x)
            y = "#".join([arr[i] for i in range(N) if i != idx])
            tmp = None
            for t in range(1, n + 1):
                for l in range(0, n - t + 1):
                    c = x[l:l+t]
                    if c not in y:
                        if tmp is None:
                            tmp = c
                        else:
                            tmp = min(tmp, c)
                if tmp is not None:
                    res.append(tmp)
                    break
            if tmp is None:
                res.append("")
        return res
