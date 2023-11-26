# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-11-26 12:17:14
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-11-26 12:17:25

"""
100134. 统计美丽子字符串 I 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个字符串 s 和一个正整数 k 。

用 vowels 和 consonants 分别表示字符串中元音字母和辅音字母的数量。

如果某个字符串满足以下条件，则称其为 美丽字符串 ：

vowels == consonants，即元音字母和辅音字母的数量相等。
(vowels * consonants) % k == 0，即元音字母和辅音字母的数量的乘积能被 k 整除。
返回字符串 s 中 非空美丽子字符串 的数量。

子字符串是字符串中的一个连续字符序列。

英语中的 元音字母 为 'a'、'e'、'i'、'o' 和 'u' 。

英语中的 辅音字母 为除了元音字母之外的所有字母。

 

示例 1：

输入：s = "baeyh", k = 2
输出：2
解释：字符串 s 中有 2 个美丽子字符串。
- 子字符串 "baeyh"，vowels = 2（["a","e"]），consonants = 2（["y","h"]）。
可以看出字符串 "aeyh" 是美丽字符串，因为 vowels == consonants 且 vowels * consonants % k == 0 。
- 子字符串 "baeyh"，vowels = 2（["a","e"]），consonants = 2（["b","y"]）。
可以看出字符串 "baey" 是美丽字符串，因为 vowels == consonants 且 vowels * consonants % k == 0 。
可以证明字符串 s 中只有 2 个美丽子字符串。
示例 2：

输入：s = "abba", k = 1
输出：3
解释：字符串 s 中有 3 个美丽子字符串。
- 子字符串 "abba"，vowels = 1（["a"]），consonants = 1（["b"]）。
- 子字符串 "abba"，vowels = 1（["a"]），consonants = 1（["b"]）。
- 子字符串 "abba"，vowels = 2（["a","a"]），consonants = 2（["b","b"]）。
可以证明字符串 s 中只有 3 个美丽子字符串。
示例 3：

输入：s = "bcdf", k = 1
输出：0
解释：字符串 s 中没有美丽子字符串。
 

提示：

1 <= s.length <= 1000
1 <= k <= 1000
s 仅由小写英文字母组成。
"""
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        v = "aeiou"
        m = 2
        while (m // 2) * (m // 2) % k:
            m += 1
        count = {0: {0: 1}}
        n = len(s)
        sum = 0
        ans = 0
        for i in range(n):
            sum += 1 if s[i] in v else -1
            if sum not in count:
                count[sum] = {}
            if (i + 1) % m not in count[sum]:
                count[sum][(i + 1) % m] = 0
            ans += count[sum][(i + 1) % m]
            count[sum][(i + 1) % m] += 1
        return ans