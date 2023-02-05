"""
6345. 重排水果 显示英文描述 
通过的用户数3
尝试过的用户数16
用户总通过次数3
用户总提交次数21
题目难度Hard
你有两个果篮，每个果篮中有 n 个水果。给你两个下标从 0 开始的整数数组 basket1 和 basket2 ，用以表示两个果篮中每个水果的成本。

你希望两个果篮相等。为此，可以根据需要多次执行下述操作：

选中两个下标 i 和 j ，并交换 basket1 中的第 i 个水果和 basket2 中的第 j 个水果。
交换的成本是 min(basket1i,basket2j) 。
根据果篮中水果的成本进行排序，如果排序后结果完全相同，则认为两个果篮相等。

返回使两个果篮相等的最小交换成本，如果无法使两个果篮相等，则返回 -1 。

 

示例 1：

输入：basket1 = [4,2,2,2], basket2 = [1,4,1,2]
输出：1
解释：交换 basket1 中下标为 1 的水果和 basket2 中下标为 0 的水果，交换的成本为 1 。此时，basket1 = [4,1,2,2] 且 basket2 = [2,4,1,2] 。重排两个数组，发现二者相等。
示例 2：

输入：basket1 = [2,3,4,1], basket2 = [3,2,5,1]
输出：-1
解释：可以证明无法使两个果篮相等。
 

提示：

basket1.length == bakste2.length
1 <= basket1.length <= 105
1 <= basket1i,basket2i <= 109
"""
class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        c = Counter(basket1 + basket2)
        c1 = Counter(basket1)
        n, x, y = 0, float("inf"), float("inf")
        n1, n2 = [], []
        for ii, jj in c.items():
            if jj % 2 == 1:
                return -1
            if jj // 2 != c1[ii]:
                n += abs(jj // 2 - c1[ii])
                x = min(x, ii)
                if jj // 2 > c1[ii]:
                    n1.extend([ii] * abs(jj // 2 - c1[ii]))
                else:
                    n2.extend([ii] * abs(jj // 2 - c1[ii]))
            else:
                y = min(y, ii)
        n //= 2
        res = n * y * 2
        # print(res, x, y, n)
        for ii, jj in c.items():
            if jj // 2 != c1[ii]:
                z = abs(jj // 2 - c1[ii])
                z = (n - z) * ii * 2 + ii * z
                res = min(res, z)
        n1 = sorted(n1)
        n2 = sorted(n2, reverse=True)
        return min(res, sum([min(i, j, 2 * y) for i, j in zip(n1, n2)]))
            
        
#         def dfs(x):
#             if n2[basket2[x]] != 0:
#                 return min(basket2[x], basket1[x]), x
#             res = float('inf')
#             c = min(basket2[x], basket1[x])
#             c2 = None
#             for y in g[basket2[x]]:
#                 c1, c3 = dfs(y)
#                 if c + c1 < res:
#                     res, c2 = c + c1, c3
#             return res, c2
#         c = Counter(basket1 + basket2)
#         c1 = Counter(basket1)
#         c2 = Counter(basket2)
#         n1, n2 = defaultdict(int), defaultdict(int)
#         for ii, jj in c.items():
#             if jj % 2 == 1:
#                 return -1
#             if jj // 2 != c1[ii]:
#                 n1[ii] = - jj // 2 + c1[ii]
#                 n2[ii] = - jj // 2 + c2[ii]
                
#         q = []
#         for (kk, ii), jj in zip(enumerate(basket1), basket2):
#             if n1[ii] != 0 and n2[jj] != 0: 
#                 heapq.heappush(q, (min(ii, jj), -max(ii, jj), ii, jj, kk))
#         res = 0
#         print(q, n1, n2)
#         while q:
#             c, _, x, y, kk = heapq.heappop(q)
#             if n1[x] == 0:
#                 continue
#             res += c
#             n1[x] -= 1
#             n1[y] += 1
#             n2[y] -= 1
#             n2[x] += 1
#             # print(n1, n2)
#             basket1[kk], basket2[kk] = basket2[kk], basket1[kk]
        
#         g = defaultdict(list)
#         for ii, jj in enumerate(basket1):
#             g[jj].append(ii)
#         q = []
#         for ii, jj in enumerate(basket1):
#             if n1[jj] != 0:
#                 heapq.heappush(q, (*dfs(ii), ii))
#         print(q)
#         while q:
#             z, y, x = heapq.heappop(q)
#             x = basket1[x]
#             if n1[x] != 0:
#                 n1[x] -= 1
#                 n1[y] += 1
#                 n2[y] -= 1
#                 n2[x] += 1
#                 res += z
#         return res
        
        
        
            