# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-10-03 00:24:17
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-10-03 00:24:32

"""
5873. 考试的最大困扰度 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
一位老师正在出一场由 n 道判断题构成的考试，每道题的答案为 true （用 'T' 表示）或者 false （用 'F' 表示）。老师想增加学生对自己做出答案的不确定性，方法是 最大化 有 连续相同 结果的题数。（也就是连续出现 true 或者连续出现 false）。

给你一个字符串 answerKey ，其中 answerKey[i] 是第 i 个问题的正确结果。除此以外，还给你一个整数 k ，表示你能进行以下操作的最多次数：

每次操作中，将问题的正确答案改为 'T' 或者 'F' （也就是将 answerKey[i] 改为 'T' 或者 'F' ）。
请你返回在不超过 k 次操作的情况下，最大 连续 'T' 或者 'F' 的数目。

 

示例 1：

输入：answerKey = "TTFF", k = 2
输出：4
解释：我们可以将两个 'F' 都变为 'T' ，得到 answerKey = "TTTT" 。
总共有四个连续的 'T' 。
示例 2：

输入：answerKey = "TFFT", k = 1
输出：3
解释：我们可以将最前面的 'T' 换成 'F' ，得到 answerKey = "FFFT" 。
或者，我们可以将第二个 'T' 换成 'F' ，得到 answerKey = "TFFF" 。
两种情况下，都有三个连续的 'F' 。
示例 3：

输入：answerKey = "TTFTTFTT", k = 1
输出：5
解释：我们可以将第一个 'F' 换成 'T' ，得到 answerKey = "TTTTTFTT" 。
或者我们可以将第二个 'F' 换成 'T' ，得到 answerKey = "TTFTTTTT" 。
两种情况下，都有五个连续的 'T' 。
 

提示：

n == answerKey.length
1 <= n <= 5 * 104
answerKey[i] 要么是 'T' ，要么是 'F'
1 <= k <= n
"""
import bisect


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        N = len(answerKey)
        idx = 0
        T, F, flag = [], [], False
        while idx < N:
            b = idx
            while idx + 1 < N and answerKey[idx + 1] == answerKey[b]:
                idx += 1
            if answerKey[b] == "T":
                T.append(idx - b + 1)
                if b == 0:
                    flag = True
            else:
                F.append(idx - b + 1)
            idx += 1
        if flag:
            T, F = F, T
        TS, FS = [0], [0]
        res = 0
        for ii in T:
            TS.append(TS[-1] + ii)
        for ii in F:
            FS.append(FS[-1] + ii)
        # print(T, TS)
        # print(F, FS)
        for x in range(len(T)):
            e_idx = bisect.bisect_left(TS, TS[x] + k)
            tmp = min(k, TS[min(e_idx, len(TS) - 1)] - TS[x])
            if tmp == TS[min(e_idx, len(TS) - 1)] - TS[x]:
                F_sum = FS[min(e_idx + 1, len(FS) - 1)] - FS[x]
            else:
                F_sum = FS[min(e_idx, len(FS) - 1)] - FS[x]
            if tmp < k and TS[-1] >= k:
                tmp = k

            # print(x, e_idx, F_sum, k, tmp)
            if F_sum + tmp > res:
                res = F_sum + tmp

        for x in range(len(F)):

            e_idx = bisect.bisect_left(FS, FS[x] + k)
            tmp = min(k, FS[min(e_idx, len(FS) - 1)] - FS[x])
            if tmp == FS[min(e_idx, len(FS) - 1)] - FS[x]:
                T_sum = TS[min(e_idx, len(TS) - 1)] - TS[max(x - 1, 0)]
            else:
                T_sum = TS[min(e_idx - 1, len(TS) - 1)] - TS[max(x - 1, 0)]
            if tmp < k and FS[-1] >= k:
                tmp = k

            # print(x, e_idx, T_sum, k, tmp)
            if T_sum + tmp > res:
                res = T_sum + tmp
        return res
