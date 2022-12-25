"""
6270. 每种字符至少取 K 个 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个由字符 'a'、'b'、'c' 组成的字符串 s 和一个非负整数 k 。每分钟，你可以选择取走 s 最左侧 还是 最右侧 的那个字符。

你必须取走每种字符 至少 k 个，返回需要的 最少 分钟数；如果无法取到，则返回 -1 。

 

示例 1：

输入：s = "aabaaaacaabc", k = 2
输出：8
解释：
从 s 的左侧取三个字符，现在共取到两个字符 'a' 、一个字符 'b' 。
从 s 的右侧取五个字符，现在共取到四个字符 'a' 、两个字符 'b' 和两个字符 'c' 。
共需要 3 + 5 = 8 分钟。
可以证明需要的最少分钟数是 8 。
示例 2：

输入：s = "a", k = 1
输出：-1
解释：无法取到一个字符 'b' 或者 'c'，所以返回 -1 。
 

提示：

1 <= s.length <= 105
s 仅由字母 'a'、'b'、'c' 组成
0 <= k <= s.length
"""
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        def is_ok():
            return c["a"] >= k and c["b"] >= k and c["c"] >= k
        res = 0
        N = len(s)
        l, r = -1, N
        c = defaultdict(int)
        while r > 0 and not is_ok():
            r -= 1
            c[s[r]] += 1
        if not is_ok():
            return -1
        # print(l, r, c)
        res = N - r
        for l in range(N):
            c[s[l]] += 1
            while r <= l:
                c[s[r]] -= 1
                r += 1
            while r < N:
                c[s[r]] -= 1
                r += 1
                if not is_ok():
                    r -= 1
                    c[s[r]] += 1
                    break
            # print(l, r)
            if is_ok():
                res = min(res, l + 1 + N - r)
        return res
        