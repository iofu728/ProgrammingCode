"""
6050. 字符串的总引力 显示英文描述 
通过的用户数139
尝试过的用户数173
用户总通过次数152
用户总提交次数197
题目难度Hard
字符串的 引力 定义为：字符串中 不同 字符的数量。

例如，"abbca" 的引力为 3 ，因为其中有 3 个不同字符 'a'、'b' 和 'c' 。
给你一个字符串 s ，返回 其所有子字符串的总引力 。

子字符串 定义为：字符串中的一个连续字符序列。

 

示例 1：

输入：s = "abbca"
输出：28
解释："abbca" 的子字符串有：
- 长度为 1 的子字符串："a"、"b"、"b"、"c"、"a" 的引力分别为 1、1、1、1、1，总和为 5 。
- 长度为 2 的子字符串："ab"、"bb"、"bc"、"ca" 的引力分别为 2、1、2、2 ，总和为 7 。
- 长度为 3 的子字符串："abb"、"bbc"、"bca" 的引力分别为 2、2、3 ，总和为 7 。
- 长度为 4 的子字符串："abbc"、"bbca" 的引力分别为 3、3 ，总和为 6 。
- 长度为 5 的子字符串："abbca" 的引力为 3 ，总和为 3 。
引力总和为 5 + 7 + 7 + 6 + 3 = 28 。
示例 2：

输入：s = "code"
输出：20
解释："code" 的子字符串有：
- 长度为 1 的子字符串："c"、"o"、"d"、"e" 的引力分别为 1、1、1、1 ，总和为 4 。
- 长度为 2 的子字符串："co"、"od"、"de" 的引力分别为 2、2、2 ，总和为 6 。
- 长度为 3 的子字符串："cod"、"ode" 的引力分别为 3、3 ，总和为 6 。
- 长度为 4 的子字符串："code" 的引力为 4 ，总和为 4 。
引力总和为 4 + 6 + 6 + 4 = 20 。
 

提示：

1 <= s.length <= 105
s 由小写英文字母组成
"""
class Solution:
    def appealSum(self, s: str) -> int:
        N = len(s)
        c = defaultdict(list)
        for ii, jj in enumerate(s):
            c[jj].append(ii)
        M = len(c)
        res = 0
        for ii in range(N):
            tmp = []
            for jj, k in c.items():
                kk = bisect.bisect_left(k, ii)
                if kk < len(k):
                    tmp.append(k[kk])
            tmp.append(N)
            tmp = sorted(tmp)
            # print(ii, tmp)
            for jj in range(1, len(tmp)):
                res += (tmp[jj] - tmp[jj - 1]) * (jj)
                # print((tmp[jj] - tmp[jj - 1]) * (jj))

        return res
    
class Solution:
    def appealSum(self, s: str) -> int:
        ans, sum_g, pos = 0, 0, [-1] * 26
        for i, c in enumerate(s):
            c = ord(c) - ord('a')
            sum_g += i - pos[c]
            ans += sum_g
            pos[c] = i
        return ans

                

