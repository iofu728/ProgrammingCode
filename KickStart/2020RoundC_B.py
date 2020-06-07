# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-05-17 19:16:13
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-05-17 19:45:53

"""

Stable Wall (8pts, 13pts)

Competitive Submissions
You have not attempted this problem.
Last updated: May 17 2020, 19:15

Problem
Apollo is playing a game involving polyominos. A polyomino is a shape made by joining together one or more squares edge to edge to form a single connected shape. The game involves combining N polyominos into a single rectangular shape without any holes. Each polyomino is labeled with a unique character from A to Z.

Apollo has finished the game and created a rectangular wall containing R rows and C columns. He took a picture and sent it to his friend Selene. Selene likes pictures of walls, but she likes them even more if they are stable walls. A wall is stable if it can be created by adding polyominos one at a time to the wall so that each polyomino is always supported. A polyomino is supported if each of its squares is either on the ground, or has another square below it.

Apollo would like to check if his wall is stable and if it is, prove that fact to Selene by telling her the order in which he added the polyominos.

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing the two integers R and C. Then, R lines follow, describing the wall from top to bottom. Each line contains a string of C uppercase characters from A to Z, describing that row of the wall.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is a string of N uppercase characters, describing the order in which he built them. If there is more than one such order, output any of them. If the wall is not stable, output -1 instead.

Limits
Time limit: 20 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
1 ≤ R ≤ 30.
1 ≤ C ≤ 30.
No two polyominos will be labeled with the same letter.
The input is guaranteed to be valid according to the rules described in the statement.

Test set 1
1 ≤ N ≤ 5.

Test set 2
1 ≤ N ≤ 26.

Sample

Input
 	
Output
 
4
4 6
ZOAAMM
ZOAOMM
ZOOOOM
ZZZZOM
4 4
XXOO
XFFO
XFXO
XXXO
5 3
XXX
XPX
XXX
XJX
XXX
3 10
AAABBCCDDE
AABBCCDDEE
AABBCCDDEE

  
Case #1: ZOAM
Case #2: -1
Case #3: -1
Case #4: EDCBA

  
In sample case #1, note that ZOMA is another possible answer.

In sample case #2 and sample case #3, the wall is not stable, so the answer is -1.

In sample case #4, the only possible answer is EDCBA.
"""

import sys

T = int(sys.stdin.readline().strip())



def get_stable_wall(case_id: int):
    def is_ok(a: str):
        have = set()
        for ii, line in enumerate(A):
            for jj, t in enumerate(line):
                if t == a and t not in have:
                    for qq in 
    R, C = [int(ii) for ii in sys.stdin.readline().strip().split()]
    A = [sys.stdin.readline() for _ in range(N)]
    first = set(list(A[-1]))
    flag = [[False] * C for _ in range(R)]

    print("Case #{}: {}".format(case_id, res))


for case_id in range(T):
    get_stable_wall(case_id + 1)
