# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-11-01 10:58:12
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-11-01 11:04:50

"""
5555. 统计字典序元音字符串的数目 显示英文描述 
通过的用户数796
尝试过的用户数841
用户总通过次数798
用户总提交次数885
题目难度Medium
给你一个整数 n，请返回长度为 n 、仅由元音 (a, e, i, o, u) 组成且按 字典序排列 的字符串数量。

字符串 s 按 字典序排列 需要满足：对于所有有效的 i，s[i] 在字母表中的位置总是与 s[i+1] 相同或在 s[i+1] 之前。

 

示例 1：

输入：n = 1
输出：5
解释：仅由元音组成的 5 个字典序字符串为 ["a","e","i","o","u"]
示例 2：

输入：n = 2
输出：15
解释：仅由元音组成的 15 个字典序字符串为
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"]
注意，"ea" 不是符合题意的字符串，因为 'e' 在字母表中的位置比 'a' 靠后
示例 3：

输入：n = 33
输出：66045
 

提示：

1 <= n <= 50 
"""


class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1] * 5
        idx = 1
        A = [5, 4, 3, 2, 1]
        while idx < n:
            tmp = []
            for ii in dp:
                tmp.append(ii + (tmp[-1] if tmp else 0))
            dp = tmp
            idx += 1
        return sum(dp)

