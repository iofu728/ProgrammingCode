"""
6074. 字母在字符串中的百分比 显示英文描述 
通过的用户数5521
尝试过的用户数5570
用户总通过次数5588
用户总提交次数6812
题目难度Easy
给你一个字符串 s 和一个字符 letter ，返回在 s 中等于 letter 字符所占的 百分比 ，向下取整到最接近的百分比。

 

示例 1：

输入：s = "foobar", letter = "o"
输出：33
解释：
等于字母 'o' 的字符在 s 中占到的百分比是 2 / 6 * 100% = 33% ，向下取整，所以返回 33 。
示例 2：

输入：s = "jjjj", letter = "k"
输出：0
解释：
等于字母 'k' 的字符在 s 中占到的百分比是 0% ，所以返回 0 。
 

提示：

1 <= s.length <= 100
s 由小写英文字母组成
letter 是一个小写英文字母
"""


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return int(s.count(letter) / len(s) * 100)
