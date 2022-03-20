"""
856. 括号的分数
给定一个平衡括号字符串 S，按下述规则计算该字符串的分数：

() 得 1 分。
AB 得 A + B 分，其中 A 和 B 是平衡括号字符串。
(A) 得 2 * A 分，其中 A 是平衡括号字符串。
 

示例 1：

输入： "()"
输出： 1
示例 2：

输入： "(())"
输出： 2
示例 3：

输入： "()()"
输出： 2
示例 4：

输入： "(()(()))"
输出： 6
 

提示：

S 是平衡括号字符串，且只含有 ( 和 ) 。
2 <= S.length <= 50
通过次数18,260提交次数29,008
"""


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        res = 0
        q = []
        h = 0
        for ii, jj in enumerate(s):
            if jj == "(":
                q.append((h, 0))
                h += 1
            else:
                a, b = q.pop()
                score = 1 if b == 0 else b
                if q:
                    q[-1] = (q[-1][0], q[-1][1] + 2 * score)
                else:
                    res += score
                h -= 1
        return res
