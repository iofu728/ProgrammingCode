# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-05-17 10:39:47
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-05-17 10:55:39

"""
5414. 收藏清单 显示英文描述 
通过的用户数6
尝试过的用户数7
用户总通过次数6
用户总提交次数7
题目难度Medium
给你一个数组 favoriteCompanies ，其中 favoriteCompanies[i] 是第 i 名用户收藏的公司清单（下标从 0 开始）。

请找出不是其他任何人收藏的公司清单的子集的收藏清单，并返回该清单下标。下标需要按升序排列。

示例 1：

输入：favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
输出：[0,1,4] 
解释：
favoriteCompanies[2]=["google","facebook"] 是 favoriteCompanies[0]=["leetcode","google","facebook"] 的子集。
favoriteCompanies[3]=["google"] 是 favoriteCompanies[0]=["leetcode","google","facebook"] 和 favoriteCompanies[1]=["google","microsoft"] 的子集。
其余的收藏清单均不是其他任何人收藏的公司清单的子集，因此，答案为 [0,1,4] 。
示例 2：

输入：favoriteCompanies = [["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]
输出：[0,1] 
解释：favoriteCompanies[2]=["facebook","google"] 是 favoriteCompanies[0]=["leetcode","google","facebook"] 的子集，因此，答案为 [0,1] 。
示例 3：

输入：favoriteCompanies = [["leetcode"],["google"],["facebook"],["amazon"]]
输出：[0,1,2,3]

提示：

1 <= favoriteCompanies.length <= 100
1 <= favoriteCompanies[i].length <= 500
1 <= favoriteCompanies[i][j].length <= 20
favoriteCompanies[i] 中的所有字符串 各不相同 。
用户收藏的公司清单也 各不相同 ，也就是说，即便我们按字母顺序排序每个清单， favoriteCompanies[i] != favoriteCompanies[j] 仍然成立。
所有字符串仅包含小写英文字母。
"""


class Solution:
    def peopleIndexes(self, C: List[List[str]]) -> List[int]:
        def is_in(a, b):
            # print(a, b)
            for t in a:
                if t not in b:
                    return False
            return True
        N = len(C)
        t = list(enumerate(C))
        t = sorted(t, key=lambda i: (len(i[1]), i[0]))
        res = []
        # print(t)
        for i, (idx, ii) in enumerate(t):
            flag = False
            for jj in range(i + 1, N):
                if is_in(ii, t[jj][1]):
                    flag = True
                    break
            if not flag:
                res.append(idx)
        return sorted(res)
                
        
