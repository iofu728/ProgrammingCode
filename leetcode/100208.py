"""
100208. 统计前后缀下标对 II 显示英文描述
通过的用户数96
尝试过的用户数293
用户总通过次数120
用户总提交次数552
题目难度Hard
给你一个下标从 0 开始的字符串数组 words 。

定义一个 布尔 函数 isPrefixAndSuffix ，它接受两个字符串参数 str1 和 str2 ：

当 str1 同时是 str2 的前缀（prefix）和后缀（suffix）时，isPrefixAndSuffix(str1, str2) 返回 true，否则返回 false。
例如，isPrefixAndSuffix("aba", "ababa") 返回 true，因为 "aba" 既是 "ababa" 的前缀，也是 "ababa" 的后缀，但是 isPrefixAndSuffix("abc", "abcd") 返回 false。

以整数形式，返回满足 i < j 且 isPrefixAndSuffix(words[i], words[j]) 为 true 的下标对 (i, j) 的 数量 。



示例 1：

输入：words = ["a","aba","ababa","aa"]
输出：4
解释：在本示例中，计数的下标对包括：
i = 0 且 j = 1 ，因为 isPrefixAndSuffix("a", "aba") 为 true 。
i = 0 且 j = 2 ，因为 isPrefixAndSuffix("a", "ababa") 为 true 。
i = 0 且 j = 3 ，因为 isPrefixAndSuffix("a", "aa") 为 true 。
i = 1 且 j = 2 ，因为 isPrefixAndSuffix("aba", "ababa") 为 true 。
因此，答案是 4 。
示例 2：

输入：words = ["pa","papa","ma","mama"]
输出：2
解释：在本示例中，计数的下标对包括：
i = 0 且 j = 1 ，因为 isPrefixAndSuffix("pa", "papa") 为 true 。
i = 2 且 j = 3 ，因为 isPrefixAndSuffix("ma", "mama") 为 true 。
因此，答案是 2 。
示例 3：

输入：words = ["abab","ab"]
输出：0
解释：在本示例中，唯一有效的下标对是 i = 0 且 j = 1 ，但是 isPrefixAndSuffix("abab", "ab") 为 false 。
因此，答案是 0 。


提示：

1 <= words.length <= 105
1 <= words[i].length <= 105
words[i] 仅由小写英文字母组成。
所有 words[i] 的长度之和不超过 5 * 105 。
"""

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        w = defaultdict(list)
        for ii in words:
            w[len(ii)].append(ii)
        w = {ii: Counter(jj) for ii, jj in w.items()}
        # w = Counter(words)
        c = defaultdict(int)
        res = 0
        for word in words[::-1]:
            w[len(word)][word] -= 1
            N = len(word)
            y = word[::-1]
            res += c[word]
            x, y = "", ""
            for ii in range(N):
                x += word[ii]
                y = word[N - ii - 1] + y
                if ii + 1 not in w:
                    continue
                if w[ii+1].get(x, 0) != 0 and x == y:
                    c[x] += 1
        return res
