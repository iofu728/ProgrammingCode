# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-01-14 15:17:58
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-01-14 15:18:09

"""
100207. 找出数组中的美丽下标 II 显示英文描述 
通过的用户数703
尝试过的用户数1688
用户总通过次数767
用户总提交次数5134
题目难度Hard
给你一个下标从 0 开始的字符串 s 、字符串 a 、字符串 b 和一个整数 k 。

如果下标 i 满足以下条件，则认为它是一个 美丽下标 ：

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

1 <= k <= s.length <= 5 * 105
1 <= a.length, b.length <= 5 * 105
s、a、和 b 只包含小写英文字母。
"""
class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        pos_a = self.kmp(s, a)
        pos_b = self.kmp(s, b)
        m = len(pos_b)

        # 写法一：二分 O(nlogn) 1040ms
        # ans = []
        # for i in pos_a:
        #     idx = bisect_left(pos_b, i)
        #     if idx < m and pos_b[idx] - i <= k or \
        #        idx > 0 and i - pos_b[idx-1] <= k:
        #         ans.append(i)
        # return ans
    

        # 写法二：双指针
        ans = []
        idx = 0
        for i in pos_a:
            while idx < m and pos_b[idx] < i-k:
                idx += 1
            if idx < m and abs(pos_b[idx] - i) <= k:
                ans.append(i)
        return ans

        
    # https://www.zhihu.com/question/21923021/answer/37475572
    def kmp(self, text: str, pattern: str) -> List[int]:
        m = len(pattern)
        pi = [0] * m
        c = 0
        for i in range(1, m):
            v = pattern[i]
            while c and pattern[c] != v:
                c = pi[c - 1]
            if pattern[c] == v:
                c += 1
            pi[i] = c

        res = []
        c = 0
        for i, v in enumerate(text):
            v = text[i]
            while c and pattern[c] != v:
                c = pi[c - 1]
            if pattern[c] == v:
                c += 1
            if c == len(pattern):
                res.append(i - m + 1)
                c = pi[c - 1]
        return res