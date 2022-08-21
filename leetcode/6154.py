"""
6154. 感染二叉树需要的总时间 显示英文描述 
通过的用户数24
尝试过的用户数27
用户总通过次数24
用户总提交次数29
题目难度Medium
给你一棵二叉树的根节点 root ，二叉树中节点的值 互不相同 。另给你一个整数 start 。在第 0 分钟，感染 将会从值为 start 的节点开始爆发。

每分钟，如果节点满足以下全部条件，就会被感染：

节点此前还没有感染。
节点与一个已感染节点相邻。
返回感染整棵树需要的分钟数。

 

示例 1：


输入：root = [1,5,3,null,4,10,6,9,2], start = 3
输出：4
解释：节点按以下过程被感染：
- 第 0 分钟：节点 3
- 第 1 分钟：节点 1、10、6
- 第 2 分钟：节点5
- 第 3 分钟：节点 4
- 第 4 分钟：节点 9 和 2
感染整棵树需要 4 分钟，所以返回 4 。
示例 2：


输入：root = [1], start = 1
输出：0
解释：第 0 分钟，树中唯一一个节点处于感染状态，返回 0 。
 

提示：

树中节点的数目在范围 [1, 105] 内
1 <= Node.val <= 105
每个节点的值 互不相同
树中必定存在值为 start 的节点
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def dfs(x):
            if x is None:
                return
            s.add(x.val)
            if x.left:
                g[x.val].add(x.left.val)
                g[x.left.val].add(x.val)
                dfs(x.left)
            if x.right:
                g[x.val].add(x.right.val)
                g[x.right.val].add(x.val)
                dfs(x.right)
        g = defaultdict(set)
        s = set()
        dfs(root)
        res = 0
        q = deque([(0, start)])
        
        while s:
            x, y = q.popleft()
            res = x
            s.remove(y)
            for ii in g[y]:
                if ii in s:
                    q.append((x + 1, ii))
        return res
            
        