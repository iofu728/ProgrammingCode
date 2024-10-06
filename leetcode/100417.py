# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-10-07 00:15:52
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-10-07 00:16:10

"""
100417. 移除可疑的方法 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
你正在维护一个项目，该项目有 n 个方法，编号从 0 到 n - 1。

给你两个整数 n 和 k，以及一个二维整数数组 invocations，其中 invocations[i] = [ai, bi] 表示方法 ai 调用了方法 bi。

已知如果方法 k 存在一个已知的 bug。那么方法 k 以及它直接或间接调用的任何方法都被视为 可疑方法 ，我们需要从项目中移除这些方法。

只有当一组方法没有被这组之外的任何方法调用时，这组方法才能被移除。

返回一个数组，包含移除所有 可疑方法 后剩下的所有方法。你可以以任意顺序返回答案。如果无法移除 所有 可疑方法，则 不 移除任何方法。

 

示例 1:

输入: n = 4, k = 1, invocations = [[1,2],[0,1],[3,2]]

输出: [0,1,2,3]

解释:



方法 2 和方法 1 是可疑方法，但它们分别直接被方法 3 和方法 0 调用。由于方法 3 和方法 0 不是可疑方法，我们无法移除任何方法，故返回所有方法。

示例 2:

输入: n = 5, k = 0, invocations = [[1,2],[0,2],[0,1],[3,4]]

输出: [3,4]

解释:



方法 0、方法 1 和方法 2 是可疑方法，且没有被任何其他方法直接调用。我们可以移除它们。

示例 3:

输入: n = 3, k = 2, invocations = [[1,2],[0,1],[2,0]]

输出: []

解释:



所有方法都是可疑方法。我们可以移除它们。

 

提示:

1 <= n <= 105
0 <= k <= n - 1
0 <= invocations.length <= 2 * 105
invocations[i] == [ai, bi]
0 <= ai, bi <= n - 1
ai != bi
invocations[i] != invocations[j]
"""
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        
        # Step 1: Initialize the graphs
        adj_list = [[] for _ in range(n)]        # Forward graph
        reverse_adj_list = [[] for _ in range(n)]  # Reverse graph

        # Step 2: Build the graphs
        for ai, bi in invocations:
            adj_list[ai].append(bi)
            reverse_adj_list[bi].append(ai)

        # Step 3: Find all suspicious methods using BFS
        suspicious = [False] * n
        queue = deque()
        queue.append(k)
        suspicious[k] = True

        while queue:
            current = queue.popleft()
            for neighbor in adj_list[current]:
                if not suspicious[neighbor]:
                    suspicious[neighbor] = True
                    queue.append(neighbor)

        # Step 4: Check if any suspicious method is called by methods outside the suspicious set
        for method in range(n):
            if suspicious[method]:
                for caller in reverse_adj_list[method]:
                    if not suspicious[caller]:
                        # Cannot remove suspicious methods
                        return list(range(n))

        # Step 5: Return the list of remaining methods
        remaining_methods = [method for method in range(n) if not suspicious[method]]
        return remaining_methods
