# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-08-06 13:38:31
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-08-06 13:38:43

"""
6932. 子序列最大优雅度 显示英文描述 
通过的用户数0
尝试过的用户数1
用户总通过次数0
用户总提交次数1
题目难度Hard
给你一个长度为 n 的二维整数数组 items 和一个整数 k 。

items[i] = [profiti, categoryi]，其中 profiti 和 categoryi 分别表示第 i 个项目的利润和类别。

现定义 items 的 子序列 的 优雅度 可以用 total_profit + distinct_categories2 计算，其中 total_profit 是子序列中所有项目的利润总和，distinct_categories 是所选子序列所含的所有类别中不同类别的数量。

你的任务是从 items 所有长度为 k 的子序列中，找出 最大优雅度 。

用整数形式表示并返回 items 中所有长度恰好为 k 的子序列的最大优雅度。

注意：数组的子序列是经由原数组删除一些元素（可能不删除）而产生的新数组，且删除不改变其余元素相对顺序。

 

示例 1：

输入：items = [[3,2],[5,1],[10,1]], k = 2
输出：17
解释：
在这个例子中，我们需要选出长度为 2 的子序列。
其中一种方案是 items[0] = [3,2] 和 items[2] = [10,1] 。
子序列的总利润为 3 + 10 = 13 ，子序列包含 2 种不同类别 [2,1] 。
因此，优雅度为 13 + 22 = 17 ，可以证明 17 是可以获得的最大优雅度。 
示例 2：

输入：items = [[3,1],[3,1],[2,2],[5,3]], k = 3
输出：19
解释：
在这个例子中，我们需要选出长度为 3 的子序列。 
其中一种方案是 items[0] = [3,1] ，items[2] = [2,2] 和 items[3] = [5,3] 。
子序列的总利润为 3 + 2 + 5 = 10 ，子序列包含 3 种不同类别 [1, 2, 3] 。 
因此，优雅度为 10 + 32 = 19 ，可以证明 19 是可以获得的最大优雅度。
示例 3：

输入：items = [[1,1],[2,1],[3,1]], k = 3
输出：7
解释：
在这个例子中，我们需要选出长度为 3 的子序列。
我们需要选中所有项目。
子序列的总利润为 1 + 2 + 3 = 6，子序列包含 1 种不同类别 [1] 。
因此，最大优雅度为 6 + 12 = 7 。
 

提示：

1 <= items.length == n <= 105
items[i].length == 2
items[i][0] == profiti
items[i][1] == categoryi
1 <= profiti <= 109
1 <= categoryi <= n
1 <= k <= n
"""
class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(key=lambda x: (-x[0], x[1]))
        g = defaultdict(list)
        for ii in range(k):
            a, b = items[ii]
            bisect.insort(g[b], -a)
        total = sum([items[ii][0] for ii in range(k)])
        c = len(g)
        c2 = c ** 2
        c2_1 = (c + 1) ** 2
        res = total + c2
        ans = res
        q = []
        for kk, v in g.items():
            if len(v) == 1:
                continue
            heapq.heappush(q, (-v[-1], kk))
        # print(items, g)
        # print(q, res, c2, c2_1, k, len(items))
        for ii in range(k, len(items)):
            if not q:
                break
            a, b = items[ii]
            # print(a, b)
            if b in g:
                continue
            z, idx = heapq.heappop(q)
            benifit = c2_1 + a - (z + c2)
            # print(benifit, c2_1, a, z, c2)
            g[b] = [a]
            g[idx].pop()
            if len(g[idx]) > 1:
                heapq.heappush(q, (-g[idx][-1], idx))
            c += 1
            c2 = c2_1
            c2_1 = (c + 1) ** 2
            res += benifit
            ans = max(res, ans)
                
        
        return ans