# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-02-23 11:46:22
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-02-23 11:46:50

import time

"""
5169. Number of Days Between Two Dates
User Accepted:3150
User Tried:3570
Total Accepted:3211
Total Submissions:6485
Difficulty:Easy
Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

 

Example 1:

Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1
Example 2:

Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15
 

Constraints:

The given dates are valid dates between the years 1971 and 2100.
"""


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date_stamp1 = self.time_stamp(date1)
        date_stamp2 = self.time_stamp(date2)
        return int(abs(date_stamp1 - date_stamp2) // (24 * 60 * 60))

    def time_stamp(self, time_str: str = "", time_format: str = "%Y-%m-%d"):
        return time.mktime(time.strptime(time_str, time_format))
