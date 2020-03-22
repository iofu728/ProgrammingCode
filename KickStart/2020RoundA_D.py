# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-22 13:46:43
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-22 14:57:53

"""

Bundling (14pts, 21pts)

Competitive Submissions
You have not attempted this problem.
Last updated: Mar 22 2020, 13:46

Problem
Pip has N strings. Each string consists only of letters from A to Z. Pip would like to bundle their strings into groups of size K. Each string must belong to exactly one group.

The score of a group is equal to the length of the longest prefix shared by all the strings in that group. For example:
The group {RAINBOW, RANK, RANDOM, RANK} has a score of 2 (the longest prefix is 'RA').
The group {FIRE, FIREBALL, FIREFIGHTER} has a score of 4 (the longest prefix is 'FIRE').
The group {ALLOCATION, PLATE, WORKOUT, BUNDLING} has a score of 0 (the longest prefix is '').

Please help Pip bundle their strings into groups of size K, such that the sum of scores of the groups is maximized.

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing the two integers N and K. Then, N lines follow, each containing one of Pip's strings.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the maximum sum of scores possible.

Limits
Time limit: 20 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
2 ≤ N ≤ 105.
2 ≤ K ≤ N.
K divides N.
Each of Pip's strings contain at least one character.
Each string consists only of letters from A to Z.

Test set 1
Each of Pip's strings contain at most 5 characters.

Test set 2
The total number of characters in Pip's strings across all test cases is at most 2 × 106.

Samples

Input 1
 	
Output 1
 
2
2 2
KICK
START
8 2
G
G
GO
GO
GOO
GOO
GOOO
GOOO
  
Case #1: 0
Case #2: 10
  

Input 2
 	
Output 2
 
1
6 3
RAINBOW
FIREBALL
RANK
RANDOM
FIREWALL
FIREFIGHTER
  
Case #1: 6
  
Sample #1
In Case #1, Pip can achieve a total score of 0 by make the groups:
{KICK, START}, with a score of 0.

In Case #2, Pip can achieve a total score of 10 by make the groups:
{G, G}, with a score of 1.
{GO, GO}, with a score of 2.
{GOO, GOO}, with a score of 3.
{GOOO, GOOO}, with a score of 4.

Sample #2
In Case #1, Pip can achieve a total score of 6 by make the groups:
{RAINBOW, RANK, RANDOM}, with a score of 2.
{FIREBALL, FIREWALL, FIREFIGHTER}, with a score of 4.

Note #1: Only Sample #1 is a valid input for Test set 1. Consequently, Sample #1 will be used as a sample test set for your submissions.
Note #2: Unlike previous editions, in Kick Start 2020, all test sets are visible verdict test sets, meaning you receive instant feedback upon submission.
"""

import sys

T = int(sys.stdin.readline().strip())


def get_max_same(a: int):
    if not len(a):
        return -1
    num = 0
    ref = a[0]
    for ii in range(len(ref)):
        diff_num = len([1 for jj in a[1:] if ref[ii] != jj[ii]])
        if diff_num == 0:
            num += 1
        else:
            break
    return num


def get_bundling(case_id: int):
    N, K = [int(ii) for ii in sys.stdin.readline().strip().split()]
    A = [sys.stdin.readline().strip() for _ in range(N)]

    def dfs(a: list, ago: int):
        if len(a) < 2 * K:
            aa = get_max_same(a)
            # print(a, aa, ago)
            return get_max_same(a) + ago
        a_map = {}
        for ii in a:
            ti = ii[0] if len(ii) else ii
            if ti not in a_map:
                a_map[ti] = []
            a_map[ti].append(ii)
        a_num = {k: len(v) for k, v in a_map.items()}
        less_k = {k: v for k, v in a_num.items() if v < K}
        big_k = {k: v for k, v in a_num.items() if v >= K}
        # print(less_k, big_k, a_map)
        B = []
        for k, v in big_k.items():
            new_a = [ii[1:] if len(ii) > 1 else "" for ii in a_map[k] if ii != ""]
            B.append(dfs(new_a, ago + 1))
        
        if len(less_k.values()) >= K:
            # print("Less_k >= K", sum(B), ago, B)
            return sum(B) + ago
        elif len(less_k.values()) == 0:
            # print("Less_k == 0", sum(B), ago, B)
            return sum(B)
        else:
            # print("Less_k < K", sum(B), ago, B)
            return sum(B) + ago - min(B) 

    num = dfs(A, 0)
    print("Case #{}: {}".format(case_id, num))


for case_id in range(T):
    get_bundling(case_id + 1)
