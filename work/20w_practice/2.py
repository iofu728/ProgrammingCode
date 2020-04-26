# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-24 21:05:29
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-24 21:48:28

"""
[编程题]水平线-研发
时间限制：C/C++ 1秒，其他语言2秒

空间限制：C/C++ 64M，其他语言128M

伞屉国是一个以太阳能为主要发电手段的国家，因此他们国家中有着非常多的太阳能基站，链接着的基站会组合成一个发电集群。但是不幸的是伞屉国不时会遭遇滔天的洪水，当洪水淹没基站时，基站只能停止发电，同时被迫断开与相邻基站的链接。你作为伞屉国的洪水观察员，有着这样的任务：在洪水到来时，计算出发电集群被洪水淹没后被拆分成了多少个集群。

由于远古的宇宙战争的原因，伞屉文明是一个二维世界里的文明，所以你可以这样理解发电基站的位置与他们的链接关系：给你一个一维数组a，长度为n，表示了n个基站的位置高度信息。数组的第i个元素a[i]表示第i个基站的海拔高度是a[i],而下标相邻的基站才相邻并且建立链接，即x号基站与x-1号基站、x+1号基站相邻。特别的，1号基站仅与2号相邻，而n号基站仅与n-1号基站相邻。当一场海拔高度为y的洪水到来时，海拔高度小于等于y的基站都会被认为需要停止发电，同时断开与相邻基站的链接。


输入描述:
每个输入数据包含一个测试点。

第一行为一个正整数n，表示发电基站的个数 (0 < n <= 200000)

接下来一行有n个空格隔开的数字，表示n个基站的海拔高度，第i个数字a[i]即为第i个基站的海拔高度，对于任意的i(1<=i<=n),有(0 <= a[i] < 2^31-1)

接下来一行有一个正整数q(0 < q <= 200000)，表示接下来有q场洪水

接下来一行有q个整数，第j个整数y[j]表示第j场洪水的海拔为y[j],对于任意的j(1<=j<=n),有(-2^31 < y[j] < 2^31-1)

输出描述:
输出q行，每行一个整数，第j行的整数ans表示在第j场洪水中，发电基站会被分割成ans个集群。标准答案保证最后一个整数后也有换行。

输入例子1:
10
6 12 20 14 15 15 7 19 18 13 
6
15 23 19 1 17 24

输出例子1:
2
0
1
1
2
0
"""
import sys

N = int(sys.stdin.readline().strip())
A = [(int(ii), idx) for idx, ii in enumerate(sys.stdin.readline().strip().split())]
T = int(sys.stdin.readline().strip())
B = [(int(ii), idx) for idx, ii in enumerate(sys.stdin.readline().strip().split())]


def get_cluster():
    A.sort()
    B.sort()
    res, last, over, h = {}, 0, {}, 1
    for ii, idx in B:
        while last < N and A[last][0] <= ii:
            now, now_id = A[last]
            over[now_id] = 0
            if (
                (now_id == 0 and now_id == N - 1)
                or (0 < now_id < N - 1 and now_id + 1 in over and now_id - 1 in over)
                or (now_id == 0 and now_id != N - 1 and now_id + 1 in over)
                or (now_id == N - 1 and now_id and now_id - 1 in over)
            ):

                h -= 1
            if 0 < now_id < N - 1 and now_id + 1 not in over and now_id - 1 not in over:
                h += 1
            last += 1
        res[idx] = h
    for ii in sorted(res):
        print(res[ii])


get_cluster()
