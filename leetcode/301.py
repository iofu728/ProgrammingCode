# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-01-15 14:56:51
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-01-15 14:57:03

"""
301. 删除无效的括号
给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。

返回所有可能的结果。答案可以按 任意顺序 返回。

 

示例 1：

输入：s = "()())()"
输出：["(())()","()()()"]
示例 2：

输入：s = "(a)())()"
输出：["(a())()","(a)()()"]
示例 3：

输入：s = ")("
输出：[""]
 

提示：

1 <= s.length <= 25
s 由小写英文字母以及括号 '(' 和 ')' 组成
s 中至多含 20 个括号
通过次数56,515提交次数103,169
"""
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def backtrack(idx, ll, rr, l, r, curr):
            if idx == N:
                if l == 0 and r == 0:
                    res.add("".join(curr))
                return
            if s[idx] == "(" and l:
                backtrack(idx + 1, ll, rr, l - 1, r, curr)
            elif s[idx] == ")" and r:
                backtrack(idx + 1, ll, rr, l, r - 1, curr)
            curr.append(s[idx])
            if s[idx] != "(" and s[idx] != ")":
                backtrack(idx + 1, ll, rr, l, r, curr)
            elif s[idx] == "(":
                backtrack(idx + 1, ll + 1, rr, l, r, curr)
            elif ll > rr:
                backtrack(idx + 1, ll, rr + 1, l, r, curr)
            curr.pop()
        N = len(s)
        l, r, res = 0, 0, set()
        for ii in s:
            if ii == "(":
                l += 1
            elif ii == ")":
                if l:
                    l -= 1
                else:
                    r += 1
        backtrack(0, 0, 0, l, r, [])
        return list(res)