# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-02 20:41:19
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-02 21:17:56

"""
943. Find the Shortest Superstring Hard
Given an array A of strings, find any smallest string that contains each string in A as a substring.

We may assume that no string in A is substring of another string in A.

## Example 1:
Input: ["alex","loves","leetcode"]
Output: "alexlovesleetcode"
Explanation: All permutations of "alex","loves","leetcode" would also be accepted.

## Example 2:
Input: ["catg","ctaagt","gcta","ttca","atgcatc"]
Output: "gctaagttcatgcatc"

## Note:
1 <= A.length <= 12
1 <= A[i].length <= 20
 
Accepted 8,948 Submissions 21,318
"""


class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:
        N = len(A)

        def get_prefix(a: str, b: str):
            MAX_LEN = min(len(a), len(b))
            for ii in range(MAX_LEN, 0, -1):
                if a[-ii:] == b[:ii]:
                    return ii
            return 0

        dist = [
            [get_prefix(A[ii], A[jj]) if ii != jj else 0 for jj in range(N)]
            for ii in range(N)
        ]
        dp = [[0] * N for _ in range(1 << N)]
        path = [[0] * N for _ in range(1 << N)]
        for s in range(1 << N):
            for ii in range(N):
                if not s >> ii & 1:
                    continue
                for jj in range(N):
                    if ii == jj or not s >> jj & 1:
                        continue
                    if dp[s][jj] <= dp[s ^ (1 << jj)][ii] + dist[ii][jj]:
                        dp[s][jj] = dp[s ^ (1 << jj)][ii] + dist[ii][jj]
                        path[s][jj] = ii
        # print(dp, path)
        last = 0
        for ii in range(N):
            if dp[-1][ii] >= dp[-1][last]:
                last = ii
        res = A[last]
        s = (1 << N) - 1
        for ii in range(N - 1):
            tmp = last
            last = path[s][last]
            res = A[last] + res[dist[last][tmp] :]
            s ^= 1 << tmp
        return res
