# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-04-04 10:31:29
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-04-04 10:31:40

"""
5722. 截断句子 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
句子 是一个单词列表，列表中的单词之间用单个空格隔开，且不存在前导或尾随空格。每个单词仅由大小写英文字母组成（不含标点符号）。

例如，"Hello World"、"HELLO" 和 "hello world hello world" 都是句子。
给你一个句子 s​​​​​​ 和一个整数 k​​​​​​ ，请你将 s​​ 截断 ​，​​​使截断后的句子仅含 前 k​​​​​​ 个单词。返回 截断 s​​​​​​ 后得到的句子。

 

示例 1：

输入：s = "Hello how are you Contestant", k = 4
输出："Hello how are you"
解释：
s 中的单词为 ["Hello", "how" "are", "you", "Contestant"]
前 4 个单词为 ["Hello", "how", "are", "you"]
因此，应当返回 "Hello how are you"
示例 2：

输入：s = "What is the solution to this problem", k = 4
输出："What is the solution"
解释：
s 中的单词为 ["What", "is" "the", "solution", "to", "this", "problem"]
前 4 个单词为 ["What", "is", "the", "solution"]
因此，应当返回 "What is the solution"
示例 3：

输入：s = "chopper is not a tanuki", k = 5
输出："chopper is not a tanuki"
 

提示：

1 <= s.length <= 500
k 的取值范围是 [1,  s 中单词的数目]
s 仅由大小写英文字母和空格组成
s 中的单词之间由单个空格隔开
不存在前导或尾随空格
"""


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split(" ")[:k])