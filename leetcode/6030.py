# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-03-20 13:54:11
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-03-20 13:54:47

"""
6030. 由单个字符重复的最长子字符串 显示英文描述 
通过的用户数13
尝试过的用户数39
用户总通过次数13
用户总提交次数56
题目难度Hard
给你一个下标从 0 开始的字符串 s 。另给你一个下标从 0 开始、长度为 k 的字符串 queryCharacters ，一个下标从 0 开始、长度也是 k 的整数 下标 数组 queryIndices ，这两个都用来描述 k 个查询。

第 i 个查询会将 s 中位于下标 queryIndices[i] 的字符更新为 queryCharacters[i] 。

返回一个长度为 k 的数组 lengths ，其中 lengths[i] 是在执行第 i 个查询 之后 s 中仅由 单个字符重复 组成的 最长子字符串 的 长度 。

 

示例 1：

输入：s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]
输出：[3,3,4]
解释：
- 第 1 次查询更新后 s = "bbbacc" 。由单个字符重复组成的最长子字符串是 "bbb" ，长度为 3 。
- 第 2 次查询更新后 s = "bbbccc" 。由单个字符重复组成的最长子字符串是 "bbb" 或 "ccc"，长度为 3 。
- 第 3 次查询更新后 s = "bbbbcc" 。由单个字符重复组成的最长子字符串是 "bbbb" ，长度为 4 。
因此，返回 [3,3,4] 。
示例 2：

输入：s = "abyzz", queryCharacters = "aa", queryIndices = [2,1]
输出：[2,3]
解释：
- 第 1 次查询更新后 s = "abazz" 。由单个字符重复组成的最长子字符串是 "zz" ，长度为 2 。
- 第 2 次查询更新后 s = "aaazz" 。由单个字符重复组成的最长子字符串是 "aaa" ，长度为 3 。
因此，返回 [2,3] 。
 

提示：

1 <= s.length <= 105
s 由小写英文字母组成
k == queryCharacters.length == queryIndices.length
1 <= k <= 105
queryCharacters 由小写英文字母组成
0 <= queryIndices[i] < s.length
"""


class Solution:
    def longestRepeating(
        self, s: str, queryCharacters: str, queryIndices: List[int]
    ) -> List[int]:
        def check(a, l, r, x):
            if l not in c or r not in e:
                return False
            rr, xx = c[l]
            if rr != r or xx != x:
                return False
            ll, xx = e[r]
            if xx != x or ll != l:
                return False
            return True

        q = []
        c, e, m = {}, {}, defaultdict(list)
        res = [0] * len(queryIndices)
        idx = 0
        N = len(s)
        while idx < N:
            l, r = idx, idx
            while r < N - 1 and s[r + 1] == s[l]:
                r += 1
            c[l] = (r, s[l])
            e[r] = (l, s[l])
            m[s[l]].append(l)
            idx = r + 1
            heapq.heappush(q, (-(r - l + 1), l, r, s[l]))
        s = {ii: jj for ii, jj in enumerate(s)}
        # print(q)
        for (idx, ii), jj in zip(enumerate(queryIndices), queryCharacters):
            if s[ii] == jj:
                a, l, r, x = heapq.heappop(q)
                while q and not check(a, l, r, x):
                    a, l, r, x = heapq.heappop(q)
                res[idx] = -a
                heapq.heappush(q, (a, l, r, x))
                s[ii] = jj
                continue
            k = bisect.bisect_left(m[s[ii]], ii)
            # print(m[s[ii]], ii, k)
            if k >= len(m[s[ii]]) or m[s[ii]][k] != ii:
                k -= 1

            o_l = m[s[ii]][k]
            o_r, _ = c[o_l]

            if o_l == ii:
                l, r = ii, ii
                r_idx = bisect.bisect_left(m[s[ii]], ii)
                m[s[ii]].pop(r_idx)
                del c[l]
                if o_r == ii:
                    del e[r]
                if ii > 0 and jj == s[ii - 1]:
                    l, _ = e[ii - 1]
                    del e[ii - 1]
                if ii < N - 1 and jj == s[ii + 1]:
                    r, _ = c[ii + 1]
                    while ii + 1 in m[s[ii + 1]]:
                        r_idx = bisect.bisect_left(m[s[ii + 1]], ii + 1)
                        m[s[ii + 1]].pop(r_idx)

                    # print(m[s[ii + 1]])
                    del c[ii + 1]
                heapq.heappush(q, (-(r - l + 1), l, r, jj))
                c[l] = (r, jj)
                e[r] = (l, jj)
                bisect.insort(m[jj], l)
                # print(")", m[jj])
                if o_r != ii:
                    heapq.heappush(q, (-(o_r - ii), ii + 1, o_r, s[ii + 1]))
                    c[ii + 1] = (o_r, s[ii + 1])
                    e[o_r] = (ii + 1, s[ii + 1])
                    bisect.insort(m[s[ii + 1]], ii + 1)
                    # print("=", m[s[ii + 1]])
            else:
                l, r = o_l, ii - 1
                heapq.heappush(q, (-(r - l + 1), l, r, s[l]))
                c[l] = (r, s[l])
                e[r] = (l, s[l])
                # bisect.insort(m[s[l]], l)
                l, r = ii, ii
                if ii == o_r:
                    if ii < N - 1 and jj == s[ii + 1]:
                        r, _ = c[ii + 1]
                        while ii + 1 in m[s[ii + 1]]:
                            r_idx = bisect.bisect_left(m[s[ii + 1]], ii + 1)
                            m[s[ii + 1]].pop(r_idx)
                        del c[ii + 1]
                else:
                    l, r = ii + 1, o_r
                    heapq.heappush(q, (-(r - l + 1), l, r, s[l]))
                    c[l] = (r, s[l])
                    e[r] = (l, s[l])
                    # print("+", m[s[l]])
                    bisect.insort(m[s[l]], l)
                    l, r = ii, ii
                heapq.heappush(q, (-(r - l + 1), l, r, jj))
                c[l] = (r, jj)
                e[r] = (l, jj)
                bisect.insort(m[jj], l)
                # print("-", m[jj])
            # print(ii, jj, "".join([s[ii] for ii in range(N)]), q)
            a, l, r, x = heapq.heappop(q)
            while q and not check(a, l, r, x):
                print(a, l, r, x, c, e)
                a, l, r, x = heapq.heappop(q)
            res[idx] = -a
            heapq.heappush(q, (a, l, r, x))
            s[ii] = jj

            # if idx > 3:
            #     break
        return res
