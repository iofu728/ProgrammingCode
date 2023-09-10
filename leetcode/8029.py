# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-09-10 13:29:55
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-09-10 13:30:07

"""
8029. 与车相交的点 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你一个下标从 0 开始的二维整数数组 nums 表示汽车停放在数轴上的坐标。对于任意下标 i，nums[i] = [starti, endi] ，其中 starti 是第 i 辆车的起点，endi 是第 i 辆车的终点。

返回数轴上被车 任意部分 覆盖的整数点的数目。

 

示例 1：

输入：nums = [[3,6],[1,5],[4,7]]
输出：7
解释：从 1 到 7 的所有点都至少与一辆车相交，因此答案为 7 。
示例 2：

输入：nums = [[1,3],[5,8]]
输出：7
解释：1、2、3、5、6、7、8 共计 7 个点满足至少与一辆车相交，因此答案为 7 。
 

提示：

1 <= nums.length <= 100
nums[i].length == 2
1 <= starti <= endi <= 100

"""
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        res, y = 0, 0
        for s, e in sorted(nums, key=lambda i:(i[0], -i[1])):
            s = max(s, y + 1)
            if e >= s:
                res += (e - s) + 1
            y = max(y, e)
        return res