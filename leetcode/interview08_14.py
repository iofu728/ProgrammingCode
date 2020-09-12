# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-12 22:04:53
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-12 22:05:09

"""
面试题 08.14. 布尔运算
给定一个布尔表达式和一个期望的布尔结果 result，布尔表达式由 0 (false)、1 (true)、& (AND)、 | (OR) 和 ^ (XOR) 符号组成。实现一个函数，算出有几种可使该表达式得出 result 值的括号方法。

示例 1:

输入: s = "1^0|0|1", result = 0

输出: 2
解释: 两种可能的括号方法是
1^(0|(0|1))
1^((0|0)|1)
示例 2:

输入: s = "0&0&0&1^1|0", result = 1

输出: 10
提示：

运算符的数量不超过 19 个
通过次数1,591提交次数3,183
"""

from functools import lru_cache


class Solution:
    AND = "&"
    OR = "|"
    XOR = "^"

    @lru_cache(None)
    def countEval(self, s: str, result: int) -> int:
        if len(s) <= 3:
            return int(eval(s) == result)
        res = 0
        for ii in range(1, len(s), 2):
            tmp = s[ii]
            if result == 0:
                if tmp == self.AND:  ## 0&0 0&1 1&0
                    res += (
                        self.countEval(s[:ii], 0) * self.countEval(s[ii + 1 :], 0)
                        + self.countEval(s[:ii], 1) * self.countEval(s[ii + 1 :], 0)
                        + self.countEval(s[:ii], 0) * self.countEval(s[ii + 1 :], 1)
                    )
                elif tmp == self.OR:  ## 0|0
                    res += self.countEval(s[:ii], 0) * self.countEval(s[ii + 1 :], 0)
                else:  ## 0^0 1^1
                    res += self.countEval(s[:ii], 0) * self.countEval(
                        s[ii + 1 :], 0
                    ) + self.countEval(s[:ii], 1) * self.countEval(s[ii + 1 :], 1)
            else:
                if tmp == self.AND:  ## 1&1
                    res += self.countEval(s[:ii], 1) * self.countEval(s[ii + 1 :], 1)
                elif tmp == self.OR:  ## 0|1 1|0 1|1
                    res += (
                        self.countEval(s[:ii], 0) * self.countEval(s[ii + 1 :], 1)
                        + self.countEval(s[:ii], 1) * self.countEval(s[ii + 1 :], 0)
                        + self.countEval(s[:ii], 1) * self.countEval(s[ii + 1 :], 1)
                    )
                else:  # 0^1 1^0
                    res += self.countEval(s[:ii], 1) * self.countEval(
                        s[ii + 1 :], 0
                    ) + self.countEval(s[:ii], 0) * self.countEval(s[ii + 1 :], 1)
        return int(res)
