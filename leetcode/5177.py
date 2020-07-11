# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-11 22:32:28
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-11 22:36:30

"""
5177. 转变日期格式 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你一个字符串 date ，它的格式为 Day Month Year ，其中：

Day 是集合 {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"} 中的一个元素。
Month 是集合 {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"} 中的一个元素。
Year 的范围在 ​[1900, 2100] 之间。
请你将字符串转变为 YYYY-MM-DD 的格式，其中：

YYYY 表示 4 位的年份。
MM 表示 2 位的月份。
DD 表示 2 位的天数。
 

示例 1：

输入：date = "20th Oct 2052"
输出："2052-10-20"
示例 2：

输入：date = "6th Jun 1933"
输出："1933-06-06"
示例 3：

输入：date = "26th May 1960"
输出："1960-05-26"
 

提示：

给定日期保证是合法的，所以不需要处理异常输入。
"""


class Solution:
    def reformatDate(self, date: str) -> str:
        MONTHS = {
            jj: ii + 1
            for ii, jj in enumerate(
                [
                    "Jan",
                    "Feb",
                    "Mar",
                    "Apr",
                    "May",
                    "Jun",
                    "Jul",
                    "Aug",
                    "Sep",
                    "Oct",
                    "Nov",
                    "Dec",
                ]
            )
        }
        day, month, year = date.split()
        day = day[:2] if day[1].isdigit() else day[0]
        month = MONTHS[month]
        return "{}-{:02d}-{:02d}".format(year, int(month), int(day))
