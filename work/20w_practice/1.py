# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-24 20:55:41
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-24 21:05:22

"""
[编程题]二进制计数-研发
时间限制：C/C++ 1秒，其他语言2秒

空间限制：C/C++ 64M，其他语言128M

小A刚学了二进制，他十分激动。为了确定他的确掌握了二进制，你给他出了这样一道题目：给定N个非负整数，将这N个数字按照二进制下1的个数分类，二进制下1的个数相同的数字属于同一类。求最后一共有几类数字？


输入描述:
输入的第一行是一个正整数T（0<T<=10），表示样例个数。对于每一个样例，第一行是一个正整数N（0<N<=100），表示有多少个数字。接下来一行是N个由空格分隔的非负整数，大小不超过2^31 – 1。，

输出描述:
对于每一组样例，输出一个正整数，表示输入的数字一共有几类。

输入例子1:
1
5
8 3 5 7 2

输出例子1:
3
"""
import sys

T = int(sys.stdin.readline().strip())


def get_bin_class(case_id: int):
    N = int(sys.stdin.readline().strip())
    A = [int(ii) for ii in sys.stdin.readline().strip().split()]
    B = set([get_bin_num(ii) for ii in A])
    print(len(B))
    # print("Case #{}: {}".format(case_id, num))


def get_bin_num(num: int) -> int:
    res = 0
    while num:
        res += num >> 1 << 1 != num
        num >>= 1
    return res


for case_id in range(T):
    get_bin_class(case_id + 1)
