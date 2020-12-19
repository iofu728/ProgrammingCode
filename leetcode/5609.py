"""
5609. 统计一致字符串的数目 显示英文描述 
通过的用户数934
尝试过的用户数954
用户总通过次数938
用户总提交次数1001
题目难度Easy
给你一个由不同字符组成的字符串 allowed 和一个字符串数组 words 。如果一个字符串的每一个字符都在 allowed 中，就称这个字符串是 一致 字符串。

请你返回 words 数组中 一致 字符串的数目。

 

示例 1：

输入：allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
输出：2
解释：字符串 "aaab" 和 "baa" 都是一致字符串，因为它们只包含字符 'a' 和 'b' 。
示例 2：

输入：allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
输出：7
解释：所有字符串都是一致的。
示例 3：

输入：allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
输出：4
解释：字符串 "cc"，"acd"，"ac" 和 "d" 是一致字符串。
 

提示：

1 <= words.length <= 104
1 <= allowed.length <= 26
1 <= words[i].length <= 10
allowed 中的字符 互不相同 。
words[i] 和 allowed 只包含小写英文字母。
"""

from collections import Counter

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        A = Counter(allowed)
        num = 0
        for ii in words:
            c = Counter(ii)
            flag = True
            for k, v in c.items():
                if k not in A:
                    flag = False
                    break
            if flag:
                num += 1
        return num
        
        