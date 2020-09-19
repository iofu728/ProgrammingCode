# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-16 20:53:37
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-16 20:53:55

"""
最大的PK结果
时间限制： 3000MS
内存限制： 589824KB
题目描述：
有n（1<=n<=100000）个葫芦娃，每个葫芦娃每个月都可以从其他葫芦娃那里得到不同数量的hudos(葫芦王国特有的货币，hudos每月最多为1000000), 每个葫芦娃去年k个月收到的hudos可以用一个长度为k(3<=k<=12)的整数数组保存，现在共有n个葫芦娃，任何两个葫芦娃都可以两两PK（同一个葫芦娃也可以自己与自己PK），PK时选出每月更多hudos数值组成一个新的数组，这个新数组中的最小值为u，求所有PK的结果u的最大值。



输入描述
第一行两个整数，代表葫芦娃个数n（1<=n<=100000）和月数k（3<=k<=12）

从第二行开始，输入n行长度为k的自然数数组（数组内每个数字均大于等于0且小于等于1000000），以空格分隔

输出描述
PK结果u的最大值


样例输入
6 5
5 0 3 1 2
1 8 9 1 3
1 2 3 4 5
9 1 0 3 7
2 3 0 6 3
6 4 1 7 0
样例输出
3
"""
import sys

A, T = [int(ii) for ii in sys.stdin.readline().strip().split()]

def get_b():
    B = [[int(ii) for ii in sys.stdin.readline().strip().split()] for ii in range(A)]
    pre = max([min(ii) for ii in B])
    B_index = [sorted(enumerate([jj[ii] for jj in B]), key=lambda x:x[1]) for ii in range(T)]
    B_map = [{ii[jj][0]: jj for jj in range(A)} for ii in B_index]
    C = range(A)
    C = sorted(C, key=lambda x:sum([ii[x] for ii in B_map]))
    if len(C) >= 2:
        C1, C2 = C[-2:]
        max_c = min([max(ii, jj) for ii, jj in zip(B[C1], B[C2])])
        pre = max(pre, max_c)
    return pre

print(get_b())
    
