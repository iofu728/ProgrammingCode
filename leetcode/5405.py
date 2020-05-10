# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-05-10 10:35:38
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-05-10 10:51:24

"""
5405. 形成两个异或相等数组的三元组数目 显示英文描述 
通过的用户数376
尝试过的用户数463
用户总通过次数376
用户总提交次数494
题目难度Medium
给你一个整数数组 arr 。

现需要从数组中取三个下标 i、j 和 k ，其中 (0 <= i < j <= k < arr.length) 。

a 和 b 定义如下：

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
注意：^ 表示 按位异或 操作。

请返回能够令 a == b 成立的三元组 (i, j , k) 的数目。

示例 1：

输入：arr = [2,3,1,6,7]
输出：4
解释：满足题意的三元组分别是 (0,1,2), (0,2,2), (2,3,4) 以及 (2,4,4)
示例 2：

输入：arr = [1,1,1,1,1]
输出：10
示例 3：

输入：arr = [2,3]
输出：0
示例 4：

输入：arr = [1,3,5,7,9]
输出：3
示例 5：

输入：arr = [7,11,12,9,5,2,7,17,22]
输出：8
 

提示：

1 <= arr.length <= 300
1 <= arr[i] <= 10^8
"""


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        N = len(arr)
        basic, ret, ans = [arr[0]], arr[0], 0
        for ii in arr[1:]:
            ret ^= ii
            basic.append(ret)
        for ii in range(N):
            # print(ii, basic)
            for jj in range(N - ii - 1):
                for kk in range(jj + 1, N - ii):
                    if basic[jj] == (basic[kk] ^ basic[jj]):
                        ans += 1
            basic = [i ^ arr[ii] for i in basic[1:]]
        return ans
