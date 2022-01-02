# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-01-02 13:31:00
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-01-02 13:31:19

"""
5967. 检查是否所有 A 都在 B 之前 显示英文描述 
User Accepted:0
User Tried:0
Total Accepted:0
Total Submissions:0
Difficulty:Easy
给你一个 仅 由字符 'a' 和 'b' 组成的字符串  s 。如果字符串中 每个 'a' 都出现在 每个 'b' 之前，返回 true ；否则，返回 false 。

 

示例 1：

输入：s = "aaabbb"
输出：true
解释：
'a' 位于下标 0、1 和 2 ；而 'b' 位于下标 3、4 和 5 。
因此，每个 'a' 都出现在每个 'b' 之前，所以返回 true 。
示例 2：

输入：s = "abab"
输出：false
解释：
存在一个 'a' 位于下标 2 ，而一个 'b' 位于下标 1 。
因此，不能满足每个 'a' 都出现在每个 'b' 之前，所以返回 false 。
示例 3：

输入：s = "bbb"
输出：true
解释：
不存在 'a' ，因此可以视作每个 'a' 都出现在每个 'b' 之前，所以返回 true 。
 

提示：

1 <= s.length <= 100
s[i] 为 'a' 或 'b'
"""
class Solution:
    def checkString(self, s: str) -> bool:
        have_b = False
        for ii in s:
            if have_b and ii == "a":
                return False
            if ii == "b":
                have_b = True
        return True