# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-04-02 15:02:47
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-04-02 15:03:03

"""
420. Strong Password Checker
Hard

466

1240

Add to List

Share
A password is considered strong if the below conditions are all met:

It has at least 6 characters and at most 20 characters.
It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
It does not contain three repeating characters in a row (i.e., "...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).
Given a string password, return the minimum number of steps required to make password strong. if password is already strong, return 0.

In one step, you can:

Insert one character to password,
Delete one character from password, or
Replace one character of password with another character.
 

Example 1:

Input: password = "a"
Output: 5
Example 2:

Input: password = "aA1"
Output: 3
Example 3:

Input: password = "1337C0d3"
Output: 0
 

Constraints:

1 <= password.length <= 50
password consists of letters, digits, dot '.' or exclamation mark '!'.
Accepted
23,824
Submissions
168,139
"""
class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        N = len(password)
        a = b = c = False
        for ii in password:
            if ii.islower():
                a = True
            elif ii.isupper():
                b = True
            elif ii.isdigit():
                c = True
        score = a + b + c

        if N < 6:
            return max(6 - N, 3 - score)
        if N <= 20:
            r = cnt = 0
            now = "#"
            for ii in password:
                if ii == now:
                    cnt += 1
                else:
                    r += cnt // 3
                    cnt = 1
                    now = ii
            r += cnt // 3
            return max(r, 3 - score)
        replace, remove = 0, N - 20
        x = cnt = 0
        now = "#"
        for ii in password:
            if ii == now:
                cnt += 1
            else:
                if remove > 0 and cnt >= 3:
                    if cnt % 3 == 0:
                        remove -= 1
                        replace -= 1
                    elif cnt % 3 == 1:
                        x += 1
                replace += cnt // 3
                cnt = 1
                now = ii
        if remove > 0 and cnt >= 3:
            if cnt % 3 == 0:
                remove -= 1
                replace -= 1
            elif cnt % 3 == 1:
                x += 1
        replace += cnt // 3
        y = min(replace, x, remove // 2)
        replace -= y
        remove -= 2 * y
        z = min(replace, remove // 3)
        replace -= z
        remove -= z * 3
        return (N - 20) + max(replace, 3 - score)