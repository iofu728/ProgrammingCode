"""
6242. 二叉搜索树最近节点查询 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个 二叉搜索树 的根节点 root ，和一个由正整数组成、长度为 n 的数组 queries 。

请你找出一个长度为 n 的 二维 答案数组 answer ，其中 answer[i] = [mini, maxi] ：

mini 是树中小于等于 queries[i] 的 最大值 。如果不存在这样的值，则使用 -1 代替。
maxi 是树中大于等于 queries[i] 的 最小值 。如果不存在这样的值，则使用 -1 代替。
返回数组 answer 。

 

示例 1 ：



输入：root = [6,2,13,1,4,9,15,null,null,null,null,null,null,14], queries = [2,5,16]
输出：[[2,2],[4,6],[15,-1]]
解释：按下面的描述找出并返回查询的答案：
- 树中小于等于 2 的最大值是 2 ，且大于等于 2 的最小值也是 2 。所以第一个查询的答案是 [2,2] 。
- 树中小于等于 5 的最大值是 4 ，且大于等于 5 的最小值是 6 。所以第二个查询的答案是 [4,6] 。
- 树中小于等于 16 的最大值是 15 ，且大于等于 16 的最小值不存在。所以第三个查询的答案是 [15,-1] 。
示例 2 ：



输入：root = [4,null,9], queries = [3]
输出：[[-1,4]]
解释：树中不存在小于等于 3 的最大值，且大于等于 3 的最小值是 4 。所以查询的答案是 [-1,4] 。
 

提示：

树中节点的数目在范围 [2, 105] 内
1 <= Node.val <= 106
n == queries.length
1 <= n <= 105
1 <= queries[i] <= 106
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        # def dfs(x, v):
        #     if x is None:
        #         return
        #     if x.val == v:
        #         tmp[0] = v
        #         tmp[1] = v
        #         return
        #     if x.val > v:
        #         tmp[1] = min(tmp[1], x.val)
        #         dfs(x.left, v)
        #     else:
        #         tmp[0] = max(tmp[0], x.val)
        #         dfs(x.right, v)
        # res = []
        # for ii in queries:
        #     tmp = [-1, float("inf")]
        #     dfs(root, ii)
        #     if tmp[-1] == float("inf"):
        #         tmp[-1] = -1
        #     res.append(tmp)
        # return res
        
        g = []
        def dfs(x):
            if x is None:
                return
            dfs(x.left)
            g.append(x.val)
            dfs(x.right)
            # return dfs(x.left) + [x.val] + dfs(x.right)
        # g = dfs(root)
        dfs(root)
        res = [0] * len(queries)
        last = 0
        for jj, ii in sorted(enumerate(queries), key=lambda i:(i[1], i[0])):
            idx = bisect.bisect_left(g, ii, last)
            if 0 <= idx < len(g) and g[idx] == ii:
                res[jj] =[ii, ii]
            else:
                if idx == 0:
                    res[jj] = [-1, g[idx]]
                elif idx == len(g):
                    res[jj] = [g[idx - 1], -1]
                else:
                    res[jj] = [g[idx - 1], g[idx]]
            last = idx
        return res