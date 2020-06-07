# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-05-17 19:59:13
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-05-17 20:07:49

"""

Perfect Subarray (10pts, 19pts)

Competitive Submissions
You have not attempted this problem.
Last updated: May 17 2020, 19:32

Problem
Cristobal has an array of N (possibly negative) integers. The i-th integer in his array is Ai. A contiguous non-empty subarray of Cristobal's array is perfect if its total sum is a perfect square. A perfect square is a number that is the product of a non-negative integer with itself. For example, the first five perfect squares are 0, 1, 4, 9 and 16.

How many subarrays are perfect? Two subarrays are different if they start or end at different indices in the array, even if the subarrays contain the same values in the same order.

Input
The first line of the input gives the number of test cases, T. T test cases follow. The first line of each test case contains the integer N. The second line contains N integers describing Cristobal's array. The i-th integer is Ai.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the number of perfect subarrays.

Limits
Memory limit: 1GB.
1 ≤ T ≤ 100.
-100 ≤ Ai ≤ 100, for all i.

Test set 1
Time limit: 20 seconds.
1 ≤ N ≤ 1000.

Test set 2
Time limit: 30 seconds.
For up to 5 cases, 1 ≤ N ≤ 105.
For the remaining cases, 1 ≤ N ≤ 1000.

Sample

Input
 	
Output
 
3
3
2 2 6
5
30 30 9 1 30
4
4 0 0 16

  
Case #1: 1
Case #2: 3
Case #3: 9

  
In sample case #1, there is one perfect subarray: [2 2] whose sum is 22.

In sample case #2, there are three perfect subarrays:
[9], whose total sum is 32.
[1], whose total sum is 12.
[30 30 9 1 30], whose total sum is 102.

In sample case #3, there are nine perfect subarrays:
[4], whose total sum is 22.
[4 0], whose total sum is 22.
[4 0 0], whose total sum is 22.
[0], whose total sum is 02.
[0 0], whose total sum is 02.
[0 0 16], whose total sum is 42.
[0], whose total sum is 02.
[0 16], whose total sum is 42.
[16], whose total sum is 42.

Note: We do not recommend using interpreted/slower languages for the test set 2 of this problem.
"""


import sys

T = int(sys.stdin.readline().strip())


def get_perfect_subarray(case_id: int):
    N = int(sys.stdin.readline())
    A = [int(ii) for ii in sys.stdin.readline().strip().split()]
    res = []
    first = set(list(A[-1]))
    flag = [[False] * C for _ in range(R)]

    print("Case #{}: {}".format(case_id, res))


for case_id in range(T):
    get_perfect_subarray(case_id + 1)
