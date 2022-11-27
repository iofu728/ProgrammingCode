'''
6244. 完美分割的方案数 显示英文描述 
通过的用户数188
尝试过的用户数333
用户总通过次数217
用户总提交次数638
题目难度Hard
给你一个字符串 s ，每个字符是数字 '1' 到 '9' ，再给你两个整数 k 和 minLength 。

如果对 s 的分割满足以下条件，那么我们认为它是一个 完美 分割：

s 被分成 k 段互不相交的子字符串。
每个子字符串长度都 至少 为 minLength 。
每个子字符串的第一个字符都是一个 质数 数字，最后一个字符都是一个 非质数 数字。质数数字为 '2' ，'3' ，'5' 和 '7' ，剩下的都是非质数数字。
请你返回 s 的 完美 分割数目。由于答案可能很大，请返回答案对 109 + 7 取余 后的结果。

一个 子字符串 是字符串中一段连续字符串序列。

 

示例 1：

输入：s = "23542185131", k = 3, minLength = 2
输出：3
解释：存在 3 种完美分割方案：
"2354 | 218 | 5131"
"2354 | 21851 | 31"
"2354218 | 51 | 31"
示例 2：

输入：s = "23542185131", k = 3, minLength = 3
输出：1
解释：存在一种完美分割方案："2354 | 218 | 5131" 。
示例 3：

输入：s = "3312958", k = 3, minLength = 1
输出：1
解释：存在一种完美分割方案："331 | 29 | 58" 。
 

提示：

1 <= k, minLength <= s.length <= 1000
s 每个字符都为数字 '1' 到 '9' 之一。
'''
class Solution:
    MODS = 10 ** 9 + 7
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        @lru_cache(None)
        def dfs(l, kk):
            if N - l < minLength or kk < 1 or not s[l] or s[-1]:
                return 0
            res = 1 if kk == 1 else 0
            for jj, ii in enumerate(tmp):
                # print(ii, l + minLength)
                if ii >= l + minLength - 1 and M - jj >= kk - 1:
                    res += dfs(ii + 1, kk - 1)
            # print(l, res)
            return res % self.MODS
                    
        s = [ii in "2357" for ii in s]
        N = len(s)
        tmp = []
        for ii, jj in enumerate(s):
            if jj is False and (ii == N - 1 or (s[ii + 1] is True)):
                tmp.append(ii)
        M = len(tmp)
        # print(tmp)
        # print(n)
        return dfs(0, k)
        
                    
#         s = [ii in "2357" for ii in s]
#         if s[0] is False or s[-1] is True:
#             return 0
#         print(s)
#         N = len(s)
#         n = 0
#         last = 0
#         for ii, jj in enumerate(s):
#             # print(last, ii, jj is False, ii - last + 1 >= minLength, (ii == N - 1 or (N - ii - 1 >= minLength and s[ii + 1] is True)))
#             if jj is False and ii - last + 1 >= minLength and (ii == N - 1 or (N - ii - 1 >= minLength and s[ii + 1] is True)):
#                 # print(last, ii)
#                 last = ii + 1
#                 n += 1
#         # print(n)
                
#         return math.comb(n - 1, k - 1) % self.MODS