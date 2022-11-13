'''
6236. 不重叠回文子字符串的最大数目 显示英文描述 
通过的用户数283
尝试过的用户数467
用户总通过次数312
用户总提交次数746
题目难度Hard
给你一个字符串 s 和一个 正 整数 k 。

从字符串 s 中选出一组满足下述条件且 不重叠 的子字符串：

每个子字符串的长度 至少 为 k 。
每个子字符串是一个 回文串 。
返回最优方案中能选择的子字符串的 最大 数目。

子字符串 是字符串中一个连续的字符序列。

 

示例 1 ：

输入：s = "abaccdbbd", k = 3
输出：2
解释：可以选择 s = "abaccdbbd" 中斜体加粗的子字符串。"aba" 和 "dbbd" 都是回文，且长度至少为 k = 3 。
可以证明，无法选出两个以上的有效子字符串。
示例 2 ：

输入：s = "adbcda", k = 2
输出：0
解释：字符串中不存在长度至少为 2 的回文子字符串。
 

提示：

1 <= k <= s.length <= 2000
s 仅由小写英文字母组成
'''
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        @lru_cache(None)
        def dfs(l):
            res = 0
            if N - l < k:
                return res
            for ii in range(l + 1, l + k):
                res = max(res, dfs(ii))
            for ii in range(l + k, N + 1):
                # print(l, ii, s[l:ii])
                if s[l] == s[ii - 1]:
                    res = max(res, int(s[l: ii] == s[l:ii][::-1]) + dfs(ii))
                else:
                    res = max(res, dfs(ii))
            # print(l, res)
            return res
                
        N = len(s)
        return dfs(0)