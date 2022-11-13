'''
6235. 逐层排序二叉树所需的最少操作数目 显示英文描述 
通过的用户数340
尝试过的用户数515
用户总通过次数344
用户总提交次数600
题目难度Medium
给你一个 值互不相同 的二叉树的根节点 root 。

在一步操作中，你可以选择 同一层 上任意两个节点，交换这两个节点的值。

返回每一层按 严格递增顺序 排序所需的最少操作数目。

节点的 层数 是该节点和根节点之间的路径的边数。

 

示例 1 ：


输入：root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]
输出：3
解释：
- 交换 4 和 3 。第 2 层变为 [3,4] 。
- 交换 7 和 5 。第 3 层变为 [5,6,8,7] 。
- 交换 8 和 7 。第 3 层变为 [5,6,7,8] 。
共计用了 3 步操作，所以返回 3 。
可以证明 3 是需要的最少操作数目。
示例 2 ：


输入：root = [1,3,2,7,6,5,4]
输出：3
解释：
- 交换 3 和 2 。第 2 层变为 [2,3] 。 
- 交换 7 和 4 。第 3 层变为 [4,6,5,7] 。 
- 交换 6 和 5 。第 3 层变为 [4,5,6,7] 。
共计用了 3 步操作，所以返回 3 。 
可以证明 3 是需要的最少操作数目。
示例 3 ：


输入：root = [1,2,3,4,5,6]
输出：0
解释：每一层已经按递增顺序排序，所以返回 0 。
 

提示：

树中节点的数目在范围 [1, 105] 。
1 <= Node.val <= 105
树中的所有值 互不相同 。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def get_num(x, y):
            # print(x, y)

            res = 0
            for ii in range(len(x)):
                a, b = ii, y[ii]
                if a == b:
                    continue
                idx1, idx2 = x[ii], ii
                y[idx1], y[idx2] = y[idx2], y[idx1]
                x[b] = idx1 
                # x[]
                # x[a], x[b] = x[b], x[a]
                res += 1
            # print(res)
            return res
        g = defaultdict(list)
        q = deque([(root, 0)])
        while q:
            a, b = q.popleft()
            if a is None:
                continue
            g[b].append(a.val)
            q.append((a.left, b + 1))
            q.append((a.right, b + 1))
        res = 0
        # print(g)
        for ii, jj in g.items():
            t = {j: i for i, j in enumerate(sorted(jj))}
            j = {t[j]: i for i, j in enumerate(jj)}
            i = {j: i for i, j in j.items()}
            # print([t[i] for i in jj])
            res += get_num(j, i)
        return res