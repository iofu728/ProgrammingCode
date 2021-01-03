# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-01-03 10:36:06
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-01-03 11:03:34

'''
5642. 大餐计数 显示英文描述 
通过的用户数334
尝试过的用户数878
用户总通过次数335
用户总提交次数1792
题目难度Medium
大餐 是指 恰好包含两道不同餐品 的一餐，其美味程度之和等于 2 的幂。

你可以搭配 任意 两道餐品做一顿大餐。

给你一个整数数组 deliciousness ，其中 deliciousness[i] 是第 i​​​​​​​​​​​​​​ 道餐品的美味程度，返回你可以用数组中的餐品做出的不同 大餐 的数量。结果需要对 109 + 7 取余。

注意，只要餐品下标不同，就可以认为是不同的餐品，即便它们的美味程度相同。

 

示例 1：

输入：deliciousness = [1,3,5,7,9]
输出：4
解释：大餐的美味程度组合为 (1,3) 、(1,7) 、(3,5) 和 (7,9) 。
它们各自的美味程度之和分别为 4 、8 、8 和 16 ，都是 2 的幂。
示例 2：

输入：deliciousness = [1,1,1,3,3,3,7]
输出：15
解释：大餐的美味程度组合为 3 种 (1,1) ，9 种 (1,3) ，和 3 种 (1,7) 。
 

提示：

1 <= deliciousness.length <= 105
0 <= deliciousness[i] <= 220
'''
from collections import Counter
import math
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        c = Counter(deliciousness)
        Min, Max = min(c), max(c)
        log2Min, log2Max = int(math.log2(Min)) if Min else 0, int(math.log2(Max)) if Max else 0
        Total = [2 ** log2Min]
        for ii in range(log2Min, log2Max + 2):
            Total.append(Total[-1] << 1)
        # print(Total)
        res = 0
        for k, v in c.items():
            for idx in range(len(Total) - 1, -1, -1):
                ii = Total[idx]
                # print(ii, k, ii - k, v, c.get(ii - k, 0), res, ii - k < k, ii - k in c)
                if ii - k < 0 or ii - k <  k:
                    break

                if ii - k in c:
                    if ii - k != k:
                        res += v * c[ii - k]
                    else:
                        res += v * (v - 1) // 2
                    res %= (10 ** 9 + 7)
        return res
        
                    
            
        
        