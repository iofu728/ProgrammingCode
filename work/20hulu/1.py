# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-16 20:53:19
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-16 20:53:31

"""
不同二叉搜索树
时间限制： 3000MS
内存限制： 589824KB
题目描述：
给定整型数组，用数组中的所有元素重建一颗二叉搜索树，总共能构造出多少种不同的二叉搜索树。二叉搜索树是指一棵空树或者具有下列性质的二叉树：

· 若任意节点的左子树不空，则左子树上所有节点的值均小于它的根节点值；

· 若任意节点的右子树不空，则右子树上所有节点的值均大于或等于它的根节点值；

· 任意节点的左、右子树也分别为二叉搜索树。

提示：数组中可能有重复元素。



输入描述
第一行是一个整数 n，表示数组长度

第二行是空格分开的 n 个整数，表示数组中的元素

输入范围 0 < n <= 800

输出描述
一个整数，表示能构造出的不同二叉搜索树的数目。若结果超过 1000000007，则返回对 1000000007 取模的结果。


样例输入
3
1 2 1
样例输出
3
"""

import sys
from collections import Counter
from functools import lru_cache
MODS = 10 ** 9 + 7

def get_C(a, b):
    if b > a // 2:
        return get_C(a, a - b)
    res = 1
    for ii in range(a, a - b, -1):
        res *= ii
    for jj in range(1, b + 1):
        res /= jj
    return int(res)



def get_BST_num():
    
    T = int(sys.stdin.readline())
    A = [int(ii) for ii in sys.stdin.readline().strip().split()]
    c = Counter(A)
    keys = list(c.keys())
    M = len(keys)
    res = 1
    for k, v in c.items():
        res *= get_C(T, v)
        res %= MODS
        T -= v

    return res % MODS

    
print(get_BST_num())
    
    