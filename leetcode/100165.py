# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-01-14 15:17:14
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-01-14 15:17:23

"""
100165. 找出数组中的美丽下标 I 显示英文描述 
通过的用户数2115
尝试过的用户数2348
用户总通过次数2411
用户总提交次数5968
题目难度Medium
给你一个下标从 0 开始的字符串 s 、字符串 a 、字符串 b 和一个整数 k 。

如果下标 i 满足以下条件，则认为它是一个 美丽下标：

0 <= i <= s.length - a.length
s[i..(i + a.length - 1)] == a
存在下标 j 使得：
0 <= j <= s.length - b.length
s[j..(j + b.length - 1)] == b
|j - i| <= k
以数组形式按 从小到大排序 返回美丽下标。

 

示例 1：

输入：s = "isawsquirrelnearmysquirrelhouseohmy", a = "my", b = "squirrel", k = 15
输出：[16,33]
解释：存在 2 个美丽下标：[16,33]。
- 下标 16 是美丽下标，因为 s[16..17] == "my" ，且存在下标 4 ，满足 s[4..11] == "squirrel" 且 |16 - 4| <= 15 。
- 下标 33 是美丽下标，因为 s[33..34] == "my" ，且存在下标 18 ，满足 s[18..25] == "squirrel" 且 |33 - 18| <= 15 。
因此返回 [16,33] 作为结果。
示例 2：

输入：s = "abcd", a = "a", b = "a", k = 4
输出：[0]
解释：存在 1 个美丽下标：[0]。
- 下标 0 是美丽下标，因为 s[0..0] == "a" ，且存在下标 0 ，满足 s[0..0] == "a" 且 |0 - 0| <= 4 。
因此返回 [0] 作为结果。
 

提示：

1 <= k <= s.length <= 105
1 <= a.length, b.length <= 10
s、a、和 b 只包含小写英文字母。

"""
class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        N, n, m = len(s), len(a), len(b)
        q, res = [], []
        for ii in range(N - m + 1):
            # if s[ii] == b[0]:
                # print(ii, s[ii: ii + m], b)
            if s[ii] == b[0] and s[ii: ii + m] == b:
                q.append(ii)
        # print(q)
        for ii in range(N - n + 1):
            if s[ii] == a[0] and s[ii: ii + n] == a:
                # print(ii)
                idx = bisect.bisect(q, ii)
                flag = False
                if idx > 0:
                    if abs(ii - q[idx - 1]) <= k:
                        flag = True
                if idx < len(q):
                    if abs(ii - q[idx]) <= k:
                        flag = True
                if flag:
                    res.append(ii)
        return res
                    
                