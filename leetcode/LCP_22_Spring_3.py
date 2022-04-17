# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-04-17 01:15:07
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-04-17 01:15:39

"""
3. 二叉搜索树染色
通过的用户数826
尝试过的用户数2313
用户总通过次数874
用户总提交次数6940
题目难度Medium
欢迎各位勇者来到力扣城，本次试炼主题为「二叉搜索树染色」。

每位勇士面前设有一个二叉搜索树的模型，模型的根节点为 root，树上的各个节点值均不重复。初始时，所有节点均为蓝色。现在按顺序对这棵二叉树进行若干次操作， ops[i] = [type, x, y] 表示第 i 次操作为：

type 等于 0 时，将节点值范围在 [x, y] 的节点均染蓝
type 等于 1 时，将节点值范围在 [x, y] 的节点均染红
请返回完成所有染色后，该二叉树中红色节点的数量。

注意：

题目保证对于每个操作的 x、y 值定出现在二叉搜索树节点中
示例 1：

输入：root = [1,null,2,null,3,null,4,null,5], ops = [[1,2,4],[1,1,3],[0,3,5]]

输出：2

解释：
第 0 次操作，将值为 2、3、4 的节点染红；
第 1 次操作，将值为 1、2、3 的节点染红；
第 2 次操作，将值为 3、4、5 的节点染蓝；
因此，最终值为 1、2 的节点为红色节点，返回数量 2
image.png

示例 2：

输入：root = [4,2,7,1,null,5,null,null,null,null,6]
ops = [[0,2,2],[1,1,5],[0,4,5],[1,5,7]]

输出：5

解释：
第 0 次操作，将值为 2 的节点染蓝；
第 1 次操作，将值为 1、2、4、5 的节点染红；
第 2 次操作，将值为 4、5 的节点染蓝；
第 3 次操作，将值为 5、6、7 的节点染红；
因此，最终值为 1、2、5、6、7 的节点为红色节点，返回数量 5
image.png

提示：

1 <= 二叉树节点数量 <= 10^5
1 <= ops.length <= 10^5
ops[i].length == 3
ops[i][0] 仅为 0 or 1
0 <= ops[i][1] <= ops[i][2] <= 10^9
0 <= 节点值 <= 10^9
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def getNumber(self, root, ops):
        """
        :type root: Optional[TreeNode]
        :type ops: List[List[int]]
        :rtype: int
        """
        vs = []
        def dfs(r):
            if not r: return
            v=r.val
            vs.append(v)
            dfs(r.left)
            dfs(r.right)
        dfs(root)
        vs.sort()
        n = len(vs)
        mx=1
        while mx<=n: mx<<=1
        mk = [2]*(mx+mx)
        def setv(i, d, s, e, v):
            if s==0 and e==d-1:
                mk[i]=v
                return
            i1, i2 = i*2+1, i*2+2
            d>>=1
            if mk[i]!=2:
                mk[i1], mk[i2]=mk[i], mk[i]
                mk[i]=2
            if e<d: setv(i1, d, s, e, v)
            elif s>=d: setv(i2, d, s-d, e-d, v)
            else:
                setv(i1, d, s, d-1, v)
                setv(i2, d, 0, e-d, v)
        def getv(i, d, k):
            if mk[i]!=2: return mk[i]
            if d==1: return 0
            d>>=1
            i1, i2 = i*2+1, i*2+2
            if k<d: return getv(i1, d, k)
            else: return getv(i2, d, k-d)
            
        for o, x, y in ops:
            kx = bisect_left(vs, x)
            ky = bisect_left(vs, y)
            if o==0:
                setv(0, mx, kx, ky, 0)
            else: setv(0, mx, kx, ky, 1)
        rc=0
        for i in range(n):
            if getv(0, mx, i): rc+=1
        return rc


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from sortedcontainers import SortedList

class Solution:
    def getNumber(self, root: Optional[TreeNode], ops: List[List[int]]) -> int:
        def dfs(p):
            if not p:
                return
            dfs(p.left)
            g.append(p.val)
            dfs(p.right)
        g = []
        dfs(root)
        N = len(g)
        
        d1, d2 = defaultdict(list), defaultdict(list)
        for idx, (op, ii, jj) in enumerate(ops):
            p = bisect.bisect_left(g, ii)
            if p < N:
                d1[p].append([idx, op])
            p = bisect.bisect_right(g, jj)
            if p < N:
                d2[p].append([idx, op])
        res = 0
        s = SortedList()
        for ii in range(N):
            for jj in d1[ii]:
                s.add(jj)
            for jj in d2[ii]:
                s.remove(jj)
            if s and s[-1][1] == 1:
                res += 1
        return res
      