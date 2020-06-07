# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-05-17 18:56:08
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-05-17 19:15:12

"""
Countdown (5pts, 7pts)

Competitive Submissions
You have not attempted this problem.
Last updated: May 17 2020, 19:00

Problem
Avery has an array of N positive integers. The i-th integer of the array is Ai.

A contiguous subarray is an m-countdown if it is of length m and contains the integers m, m-1, m-2, ..., 2, 1 in that order. For example, [3, 2, 1] is a 3-countdown.

Can you help Avery count the number of K-countdowns in her array?

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing the integers N and K. The second line contains N integers. The i-th integer is Ai.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the number of K-countdowns in her array.

Limits
Time limit: 20 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
2 ≤ K ≤ N.
1 ≤ Ai ≤ 2 × 105, for all i.

Test set 1
2 ≤ N ≤ 1000.

Test set 2
2 ≤ N ≤ 2 × 105 for at most 10 test cases.
For the remaining cases, 2 ≤ N ≤ 1000.

Sample

Input
 	
Output
 
3
12 3
1 2 3 7 9 3 2 1 8 3 2 1
4 2
101 100 99 98
9 6
100 7 6 5 4 3 2 1 100

  
Case #1: 2
Case #2: 0
Case #3: 1

  
In sample case #1, there are two 3-countdowns as highlighted below.
1 2 3 7 9 3 2 1 8 3 2 1
1 2 3 7 9 3 2 1 8 3 2 1

In sample case #2, there are no 2-countdowns.

In sample case #3, there is one 6-countdown as highlighted below.
100 7 6 5 4 3 2 1 100
"""
import sys

T = int(sys.stdin.readline().strip())


def get_countdown(case_id: int):
    N, K = [int(ii) for ii in sys.stdin.readline().strip().split()]
    A = [int(ii) for ii in sys.stdin.readline().strip().split()]
    idx, res = 0, 0
    while idx < N:
        if A[idx] != K:
            idx += 1
            continue
        flag = True
        for ii in range(1, K):
            idx += 1
            if idx > N - 1 or A[idx] != K - ii:
                flag = False
                break
        if flag:
            res += 1

    print("Case #{}: {}".format(case_id, res))


for case_id in range(T):
    get_countdown(case_id + 1)
