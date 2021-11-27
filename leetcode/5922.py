# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-11-27 23:28:40
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-11-27 23:28:58

"""
5922. 统计出现过一次的公共字符串 显示英文描述 
User Accepted:0
User Tried:0
Total Accepted:0
Total Submissions:0
Difficulty:Easy
给你两个字符串数组 words1 和 words2 ，请你返回在两个字符串数组中 都恰好出现一次 的字符串的数目。

 

示例 1：

输入：words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
输出：2
解释：
- "leetcode" 在两个数组中都恰好出现一次，计入答案。
- "amazing" 在两个数组中都恰好出现一次，计入答案。
- "is" 在两个数组中都出现过，但在 words1 中出现了 2 次，不计入答案。
- "as" 在 words1 中出现了一次，但是在 words2 中没有出现过，不计入答案。
所以，有 2 个字符串在两个数组中都恰好出现了一次。
示例 2：

输入：words1 = ["b","bb","bbb"], words2 = ["a","aa","aaa"]
输出：0
解释：没有字符串在两个数组中都恰好出现一次。
示例 3：

输入：words1 = ["a","ab"], words2 = ["a","a","a","ab"]
输出：1
解释：唯一在两个数组中都出现一次的字符串是 "ab" 。
 

提示：

1 <= words1.length, words2.length <= 1000
1 <= words1[i].length, words2[j].length <= 30
words1[i] 和 words2[j] 都只包含小写英文字母。
"""
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        c1, c2 = Counter(words1), Counter(words2)
        res = 0
        for ii, jj in c1.items():
            if jj != 1:
                continue
            if c2.get(ii, 0) == 1:
                res += 1
        return res
                