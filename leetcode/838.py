"""
838. Push Dominoes
Medium

1555

102

Add to List

Share
There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.

 

Example 1:

Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
Example 2:


Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
 

Constraints:

n == dominoes.length
1 <= n <= 105
dominoes[i] is either 'L', 'R', or '.'.
Accepted
55,668
Submissions
106,764
"""


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        N = len(dominoes)
        res = list(dominoes)
        idx = 0
        L = ([-1] if dominoes[0] == "." else []) + [
            ii
            for ii in range(N - 1)
            if dominoes[ii] in "LR" and dominoes[ii + 1] == "."
        ]
        R = [
            ii for ii in range(1, N) if dominoes[ii] in "LR" and dominoes[ii - 1] == "."
        ] + ([N] if dominoes[-1] == "." else [])
        for ii, jj in zip(L, R):
            # print(ii, jj)
            if ii == -1:
                if jj == N or dominoes[jj] == "R":
                    continue
                a = b = dominoes[jj]
            elif jj == N:
                a = b = dominoes[ii]
                if a == "L":
                    continue
            else:
                a, b = dominoes[ii], dominoes[jj]
                if a == "L" and b == "R":
                    continue
            if a == b:
                idx = ii + 1
                while idx < jj:
                    res[idx] = a
                    idx += 1
            else:
                l, r = ii + 1, jj - 1
                while l < r:
                    res[l] = a
                    res[r] = b
                    l += 1
                    r -= 1
        return "".join(res)
