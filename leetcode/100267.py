# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-04-14 13:02:49
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-04-14 13:03:00

"""
100267. 单面值组合的第 K 小金额 显示英文描述 
通过的用户数2
尝试过的用户数7
用户总通过次数2
用户总提交次数10
题目难度Hard
给你一个整数数组 coins 表示不同面额的硬币，另给你一个整数 k 。

你有无限量的每种面额的硬币。但是，你 不能 组合使用不同面额的硬币。

返回使用这些硬币能制造的 第 kth 小 金额。

 

示例 1：

输入： coins = [3,6,9], k = 3

输出： 9

解释：给定的硬币可以制造以下金额：
3元硬币产生3的倍数：3, 6, 9, 12, 15等。
6元硬币产生6的倍数：6, 12, 18, 24等。
9元硬币产生9的倍数：9, 18, 27, 36等。
所有硬币合起来可以产生：3, 6, 9, 12, 15等。

示例 2：

输入：coins = [5,2], k = 7

输出：12

解释：给定的硬币可以制造以下金额：
5元硬币产生5的倍数：5, 10, 15, 20等。
2元硬币产生2的倍数：2, 4, 6, 8, 10, 12等。
所有硬币合起来可以产生：2, 4, 5, 6, 8, 10, 12, 14, 15等。

 

提示：

1 <= coins.length <= 15
1 <= coins[i] <= 25
1 <= k <= 2 * 109
coins 包含两两不同的整数。
"""
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        d = Counter()
        n = len(coins)
        def dfs(idx, v, msk):        
            if idx == n:
                d[v] += msk
                return
            dfs(idx + 1, math.lcm(v, coins[idx]), -msk)
            dfs(idx + 1, v, msk)
            
        dfs(0, 1, -1)
        d[1] += 1
        l, r = 1, 10 ** 11
        while l <= r:
            m = (l + r) // 2
            cnt = 0
            for x in d:
                cnt += m // x * d[x]
            if cnt >= k: r = m - 1
            else: l = m + 1
        return l
        
        @lru_cache(None)
        def fuc2(p, q):
            while p!=q:
                if p>q:
                    p = p - q
                else:
                    q = q - p
            return p
            
        def is_ok(x):
            res, same = 0, False
            y = [[] for ii in range(16)]
            for jj, ii in enumerate(cc):
                res += x // ii
                
                # print("+", x // ii)
                if x % ii == 0:
                    same = True
                for _ in range(15, -1, -1):
                    for yy in y[_]:
                        # print("++", yy, ii)
                        y[_ + 1].append((ii * yy // fuc2(ii, yy)))
                        
                        res += x // (ii * yy // fuc2(ii, yy)) * (1 if _ % 2 == 0 else -1)
                # for yy in y:
                    # print("++", yy, ii, x // (ii * yy // fuc2(ii, yy)))
                    # res += x // (ii * yy // fuc2(ii, yy))
                for kk in cc[:jj]:
                    # print("-", x // (ii * kk // fuc2(ii, kk)))
                    y[0].append((ii * kk // fuc2(ii, kk)))
                    res -= x // (ii * kk // fuc2(ii, kk))
                

            return res if same else res + 1, same
   
        coins = sorted(coins)
        cc = [coins[0]]
        for ii in coins[1:]:
            flag = True
            for jj in cc:
                if ii % jj == 0:
                    flag = False
                    break
            if flag:
                cc.append(ii)
        N = len(cc)
        l, r = (k // N) * cc[0], (k // N + 1) * cc[-1]
        while l < r:
            m = (l + r) // 2
            a, b = is_ok(m)
            # print(m, a, b)
            if a == k and b:
                # print(m)
                # break
                return m
            elif a <= k:
                l = m + 1
            else:
                r = m
        return l
        