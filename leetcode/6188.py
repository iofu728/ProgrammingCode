# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-09-25 12:17:20
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-09-25 12:17:41
"""
6188. 按身高排序 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你一个字符串数组 names ，和一个由 互不相同 的正整数组成的数组 heights 。两个数组的长度均为 n 。

对于每个下标 i，names[i] 和 heights[i] 表示第 i 个人的名字和身高。

请按身高 降序 顺序返回对应的名字数组 names 。

 

示例 1：

输入：names = ["Mary","John","Emma"], heights = [180,165,170]
输出：["Mary","Emma","John"]
解释：Mary 最高，接着是 Emma 和 John 。
示例 2：

输入：names = ["Alice","Bob","Bob"], heights = [155,185,150]
输出：["Bob","Alice","Bob"]
解释：第一个 Bob 最高，然后是 Alice 和第二个 Bob 。
 

提示：

n == names.length == heights.length
1 <= n <= 103
1 <= names[i].length <= 20
1 <= heights[i] <= 105
names[i] 由大小写英文字母组成
heights 中的所有值互不相同

"""
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [ii for ii, jj in sorted(zip(names, heights), key=lambda i:(-i[1]))]