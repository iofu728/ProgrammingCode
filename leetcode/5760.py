'''
5760. Minimum Number of Swaps to Make the Binary String Alternating My SubmissionsBack to Contest
User Accepted: 34
User Tried: 74
Total Accepted: 34
Total Submissions: 86
Difficulty: Medium
Given a binary string s, return the minimum number of character swaps to make it alternating, or -1 if it is impossible.

The string is called alternating if no two adjacent characters are equal. For example, the strings "010" and "1010" are alternating, while the string "0100" is not.

Any two characters may be swapped, even if they are not adjacent.

 

Example 1:

Input: s = "111000"
Output: 1
Explanation: Swap positions 1 and 4: "111000" -> "101010"
The string is now alternating.
Example 2:

Input: s = "010"
Output: 0
Explanation: The string is already alternating, no swaps are needed.
Example 3:

Input: s = "1110"
Output: -1
 

Constraints:

1 <= s.length <= 1000
s[i] is either '0' or '1'.
'''

class Solution:
    def minSwaps(self, s: str) -> int:
        def check(a: str, b: str):
            num1 = len([1 for ii in range(N // 2 + 2) if 2 * ii < N and s[2 * ii] != a])
            num2 = len([1 for ii in range(N // 2 + 2) if 2 * ii + 1 < N and s[2 * ii + 1] != b])
            return num1, num2
        N = len(s)
        res1 = check("0", "1")
        res2 = check("1", "0")
        flag1 = res1[0] == res1[1]
        flag2 = res2[0] == res2[1]
        if flag1 and not flag2:
            return res1[0]
        if flag2 and not flag1:
            return res2[0]
        if not flag1 and not flag2:
            return -1
        return min(res1[0], res2[0])

        