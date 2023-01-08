"""
6284. 使字符串总不同字符的数目相等 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你两个下标从 0 开始的字符串 word1 和 word2 。

一次 移动 由以下两个步骤组成：

选中两个下标 i 和 j ，分别满足 0 <= i < word1.length 和 0 <= j < word2.length ，
交换 word1[i] 和 word2[j] 。
如果可以通过 恰好一次 移动，使 word1 和 word2 中不同字符的数目相等，则返回 true ；否则，返回 false 。

 

示例 1：

输入：word1 = "ac", word2 = "b"
输出：false
解释：交换任何一组下标都会导致第一个字符串中有 2 个不同的字符，而在第二个字符串中只有 1 个不同字符。
示例 2：

输入：word1 = "abcc", word2 = "aab"
输出：true
解释：交换第一个字符串的下标 2 和第二个字符串的下标 0 。之后得到 word1 = "abac" 和 word2 = "cab" ，各有 3 个不同字符。
示例 3：

输入：word1 = "abcde", word2 = "fghij"
输出：true
解释：无论交换哪一组下标，两个字符串中都会有 5 个不同字符。
 

提示：

1 <= word1.length, word2.length <= 105
word1 和 word2 仅由小写英文字母组成。
"""
class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        def is_ok(a, b):
            x, y = c1.copy(), c2.copy()
            x[a] -= 1
            y[a] += 1
            x[b] += 1
            y[b] -= 1
            if x[a] == 0:
                del x[a]
            if y[b] == 0:
                del y[b]
            return len(x) == len(y)
    
        c1, c2 = Counter(word1), Counter(word2)
        for ii in c1:
            for jj in c2:
                if is_ok(ii, jj):
                    return True
        return False