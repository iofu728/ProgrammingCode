'''
100602. 子字符串连接后的最长回文串 I 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你两个字符串 s 和 t。

你可以从 s 中选择一个子串（可以为空）以及从 t 中选择一个子串（可以为空），然后将它们 按顺序 连接，得到一个新的字符串。

返回可以由上述方法构造出的 最长 回文串的长度。

回文串 是指正着读和反着读都相同的字符串。

子字符串 是指字符串中的一个连续字符序列。

 

示例 1：

输入： s = "a", t = "a"

输出： 2

解释：

从 s 中选择 "a"，从 t 中选择 "a"，拼接得到 "aa"，这是一个长度为 2 的回文串。

示例 2：

输入： s = "abc", t = "def"

输出： 1

解释：

由于两个字符串的所有字符都不同，最长的回文串只能是任意一个单独的字符，因此答案是 1。

示例 3：

输入： s = "b", t = "aaaa"

输出： 4

解释：

可以选择 "aaaa" 作为回文串，其长度为 4。

示例 4：

输入： s = "abcde", t = "ecdba"

输出： 5

解释：

从 s 中选择 "abc"，从 t 中选择 "ba"，拼接得到 "abcba"，这是一个长度为 5 的回文串。

 

提示：

1 <= s.length, t.length <= 30
s 和 t 仅由小写英文字母组成。

'''
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        def compute_is_pal(u: str):
            L = len(u)
            is_pal = [[False] * L for _ in range(L)]
            for i in range(L):
                is_pal[i][i] = True
            for i in range(L - 1):
                is_pal[i][i + 1] = (u[i] == u[i + 1])
            for length in range(3, L + 1):
                for i in range(L - length + 1):
                    j = i + length - 1
                    if u[i] == u[j] and is_pal[i + 1][j - 1]:
                        is_pal[i][j] = True
            return is_pal

        n, m = len(s), len(t)
        is_pal_s = compute_is_pal(s)
        is_pal_t = compute_is_pal(t)
        best_start_s = [0] * n
        for i in range(n):
            maxL = 0
            for j in range(i, n):
                if is_pal_s[i][j]:
                    maxL = max(maxL, j - i + 1)
            best_start_s[i] = maxL
        best_end_t = [0] * m
        for j in range(m):
            maxL = 0
            for i in range(j + 1):
                if is_pal_t[i][j]:
                    maxL = max(maxL, j - i + 1)
            best_end_t[j] = maxL
        candidate1 = max(max(best_start_s) if n > 0 else 0, max(best_end_t) if m > 0 else 0)

        r = t[::-1]
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        candidate2 = 0
        for i in range(n):
            for j in range(m):
                if s[i] == r[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                    L_common = dp[i + 1][j + 1]
                    candidate_even = 2 * L_common
                    candidate_odd_s = candidate_even
                    if i + 1 < n:
                        candidate_odd_s = 2 * L_common + best_start_s[i + 1]
                    candidate_odd_t = candidate_even
                    pos = m - 1 - j
                    if pos > 0:
                        candidate_odd_t = 2 * L_common + best_end_t[pos - 1]
                    candidate2 = max(candidate2, candidate_even, candidate_odd_s, candidate_odd_t)
                else:
                    dp[i + 1][j + 1] = 0
        return max(candidate1, candidate2)

        