# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-01-22 17:07:41
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-01-22 17:07:58

"""
1982. 从子集的和还原数组
存在一个未知数组需要你进行还原，给你一个整数 n 表示该数组的长度。另给你一个数组 sums ，由未知数组中全部 2n 个 子集的和 组成（子集中的元素没有特定的顺序）。

返回一个长度为 n 的数组 ans 表示还原得到的未知数组。如果存在 多种 答案，只需返回其中 任意一个 。

如果可以由数组 arr 删除部分元素（也可能不删除或全删除）得到数组 sub ，那么数组 sub 就是数组 arr 的一个 子集 。sub 的元素之和就是 arr 的一个 子集的和 。一个空数组的元素之和为 0 。

注意：生成的测试用例将保证至少存在一个正确答案。

 

示例 1：

输入：n = 3, sums = [-3,-2,-1,0,0,1,2,3]
输出：[1,2,-3]
解释：[1,2,-3] 能够满足给出的子集的和：
- []：和是 0
- [1]：和是 1
- [2]：和是 2
- [1,2]：和是 3
- [-3]：和是 -3
- [1,-3]：和是 -2
- [2,-3]：和是 -1
- [1,2,-3]：和是 0
注意，[1,2,-3] 的任何排列和 [-1,-2,3] 的任何排列都会被视作正确答案。
示例 2：

输入：n = 2, sums = [0,0,0,0]
输出：[0,0]
解释：唯一的正确答案是 [0,0] 。
示例 3：

输入：n = 4, sums = [0,0,5,5,4,-1,4,9,9,-1,4,3,4,8,3,8]
输出：[0,-1,4,5]
解释：[0,-1,4,5] 能够满足给出的子集的和。
 

提示：

1 <= n <= 15
sums.length == 2n
-104 <= sums[i] <= 104
通过次数944提交次数2,031
"""
class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        def dfs(n, tmp):
            if n == 1:
                if tmp[0] == 0:
                    return tmp[1:]
                if tmp[1] == 0:
                    return tmp[:1]
                return []
            print(tmp)
            d = tmp[1] - tmp[0]
            l, r, done = [], [], set()
            ll, rr = 0, 0
            while True:
                while ll < (1 << n) and ll in done:
                    ll += 1
                if ll == (1 << n):
                    break
                done.add(ll)
                while rr < (1 << n) and (rr in done or tmp[rr] != tmp[ll] + d):
                    rr += 1
                done.add(rr)
                l.append(tmp[ll])
                r.append(tmp[rr])
            res = dfs(n - 1, l)
            if res:
                return res + [d]
            res = dfs(n - 1, r)
            if res:
                return res + [-d]
            return []

        sums = sorted(sums)
        return dfs(n, sums)
