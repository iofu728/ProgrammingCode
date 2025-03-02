"""
100596. 至多 K 次操作后的最长回文子序列 显示英文描述 
通过的用户数3
尝试过的用户数6
用户总通过次数3
用户总提交次数7
题目难度Medium
给你一个字符串 s 和一个整数 k。

在一次操作中，你可以将任意位置的字符替换为字母表中相邻的字符（字母表是循环的，因此 'z' 的下一个字母是 'a'）。例如，将 'a' 替换为下一个字母结果是 'b'，将 'a' 替换为上一个字母结果是 'z'；同样，将 'z' 替换为下一个字母结果是 'a'，替换为上一个字母结果是 'y'。

返回在进行 最多 k 次操作后，s 的 最长回文子序列 的长度。

子序列 是一个 非空 字符串，可以通过删除原字符串中的某些字符（或不删除任何字符）并保持剩余字符的相对顺序得到。

回文 是正着读和反着读都相同的字符串。

 

示例 1：

输入: s = "abced", k = 2

输出: 3

解释:

将 s[1] 替换为下一个字母，得到 "acced"。
将 s[4] 替换为上一个字母，得到 "accec"。
子序列 "ccc" 形成一个长度为 3 的回文，这是最长的回文子序列。

示例 2：

输入: s = "aaazzz", k = 4

输出: 6

解释:

将 s[0] 替换为上一个字母，得到 "zaazzz"。
将 s[4] 替换为下一个字母，得到 "zaazaz"。
将 s[3] 替换为下一个字母，得到 "zaaaaz"。
整个字符串形成一个长度为 6 的回文。

 

提示:

1 <= s.length <= 200
1 <= k <= 200
s 仅由小写英文字母组成。

"""
class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        # @cache
        # def dp(l, r, m):
        #     if l > r:
        #         return 0
        #     if l == r:
        #         return 1
        #     res = max(dp(l + 1, r, m), dp(l, r - 1, m))
        #     a = ord(s[l])
        #     b = ord(s[r])
        #     c = min((a - b + 26) % 26, (b - a + 26) % 26)
        #     if c <= m:
        #         res = max(res, 2 + dp(l + 1, r - 1, m - c))
        #     return res
        
        n = len(s)
        dp = [[[0] * (k + 1) for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for m in range(k + 1):
                dp[i][i][m] = 1
        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1
                for m in range(k + 1):
                    opt1 = dp[l + 1][r][m] if l + 1 <= r else 0
                    opt2 = dp[l][r - 1][m] if l <= r - 1 else 0
                    res = max(opt1, opt2)
                    a = ord(s[l])
                    b = ord(s[r])
                    c = min((a - b + 26) % 26, (b - a + 26) % 26)
                    if c <= m:
                        if l + 1 <= r - 1:
                            res = max(res, 2 + dp[l + 1][r - 1][m - c])
                        else:
                            res = max(res, 2)
                    dp[l][r][m] = res        
            
        
        return dp[0][n - 1][k]

#         def get_dis(i, j):
#             res = 0
#             while i < j:
#                 a = ord(s[i])
#                 b = ord(s[j])
#                 res += min((a - b + 26) % 26, (b - a + 26) % 26)
#                 i += 1
#                 j -= 1
#             return res
                    
#         def is_ok(m):
#             for i in range(0, n - m + 1):
#                 j = i + m - 1
#                 if get_dis(i, j) <= k:
#                     return True
#             return False
            
#         n = len(s)
#         left, right = 1, n + 1
#         while left < right:
#             mid = (left + right) // 2
#             if is_ok(mid):
#                 left = mid + 1
#             else:
#                 right = mid
#             # print(left, right)
#         return left - 1
