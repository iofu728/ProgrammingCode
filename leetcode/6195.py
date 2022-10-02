# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-10-02 12:56:17
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-10-02 12:56:29

"""
6195. 对字母串可执行的最大删除数 显示英文描述 
通过的用户数18
尝试过的用户数23
用户总通过次数18
用户总提交次数28
题目难度Hard
给你一个仅由小写英文字母组成的字符串 s 。在一步操作中，你可以：

删除 整个字符串 s ，或者
对于满足 1 <= i <= s.length / 2 的任意 i ，如果 s 中的 前 i 个字母和接下来的 i 个字母 相等 ，删除 前 i 个字母。
例如，如果 s = "ababc" ，那么在一步操作中，你可以删除 s 的前两个字母得到 "abc" ，因为 s 的前两个字母和接下来的两个字母都等于 "ab" 。

返回删除 s 所需的最大操作数。

 

示例 1：

输入：s = "abcabcdabc"
输出：2
解释：
- 删除前 3 个字母（"abc"），因为它们和接下来 3 个字母相等。现在，s = "abcdabc"。
- 删除全部字母。
一共用了 2 步操作，所以返回 2 。可以证明 2 是所需的最大操作数。
注意，在第二步操作中无法再次删除 "abc" ，因为 "abc" 的下一次出现并不是位于接下来的 3 个字母。
示例 2：

输入：s = "aaabaab"
输出：4
解释：
- 删除第一个字母（"a"），因为它和接下来的字母相等。现在，s = "aabaab"。
- 删除前 3 个字母（"aab"），因为它们和接下来 3 个字母相等。现在，s = "aab"。 
- 删除第一个字母（"a"），因为它和接下来的字母相等。现在，s = "ab"。
- 删除全部字母。
一共用了 4 步操作，所以返回 4 。可以证明 4 是所需的最大操作数。
示例 3：

输入：s = "aaaaa"
输出：5
解释：在每一步操作中，都可以仅删除 s 的第一个字母。
 

提示：

1 <= s.length <= 4000
s 仅由小写英文字母组成
"""

class Solution:
    def deleteString(self, s: str) -> int:
        def check(y):
            n = len(y)
            for ii in range(1, n // 2 + 1):
                # print(y, ii)
                if n % ii == 0 and len(set([y[jj:jj + ii] for jj in range(0, n, ii)])) == 1:
                    return ii
            return n
        def get_x(s, t):
            # print(s, t)
            n = len(s)
            if t > self.res:
                self.res = t
            for ii in range(n // 2, 0, -1):
                # print(ii, s[:ii], s[ii:ii * 2])
                if s[:ii] == s[ii:ii * 2]:
                    
                    k = check(s[:ii])
                    # print(s[:ii], k)
                    get_x(s[k:], t + 1)
                    break
                    
        self.res = 0
        get_x(s, 0)
        return self.res + 1