# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-06-02 12:03:45
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-06-02 12:03:56

"""
100311. 无需开会的工作日 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个正整数 days，表示员工可工作的总天数（从第 1 天开始）。另给你一个二维数组 meetings，长度为 n，其中 meetings[i] = [start_i, end_i] 表示第 i 次会议的开始和结束天数（包含首尾）。

返回员工可工作且没有安排会议的天数。

注意：会议时间可能会有重叠。

 

示例 1：

输入：days = 10, meetings = [[5,7],[1,3],[9,10]]

输出：2

解释：

第 4 天和第 8 天没有安排会议。

示例 2：

输入：days = 5, meetings = [[2,4],[1,3]]

输出：1

解释：

第 5 天没有安排会议。

示例 3：

输入：days = 6, meetings = [[1,6]]

输出：0

解释：

所有工作日都安排了会议。

 

提示：

1 <= days <= 109
1 <= meetings.length <= 105
meetings[i].length == 2
1 <= meetings[i][0] <= meetings[i][1] <= days
"""
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings, key=lambda i:(i[0], -i[1]))
        last, res = 0, 0
        for ii, jj in meetings:
            if ii > last + 1:
                res += ii - (last + 1)
            last = max(last, jj)
        if last < days:
            res += days - last
        return res