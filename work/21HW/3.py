# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-01-27 21:36:26
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-01-27 21:48:03

import sys

def judgePointNum():
    A = sys.stdin.readline()
    A = [int(ii) for ii in A.split(", ")]
    B = set()
    EPSILON = 1e-6
    ADD, MULTIPLY, SUBTRACT, DIVIDE = 0, 1, 2, 3

    def solve(nums):
        if len(nums) == 1:
            if 1 <= int(nums[0]) <= 100 and nums[0] - int(nums[0]) < EPSILON:
                B.add(int(nums[0]))
            return
        if len(B) == 100:
            return
        for i, x in enumerate(nums):
            for j, y in enumerate(nums):
                if i != j:
                    newNums = list()
                    for k, z in enumerate(nums):
                        if k != i and k != j:
                            newNums.append(z)
                    for k in range(4):
                        if k < 2 and i > j:
                            continue
                        if k == ADD:
                            newNums.append(x + y)
                        elif k == MULTIPLY:
                            newNums.append(x * y)
                        elif k == SUBTRACT:
                            newNums.append(x - y)
                        elif k == DIVIDE:
                            if abs(y) < EPSILON:
                                continue
                            newNums.append(x / y)
                        solve(newNums)
                        if len(B) == 100:
                            return
                        newNums.pop()

    solve(A)
    print(len(B))

judgePointNum()