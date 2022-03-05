"""
5237. Minimum Number of Moves to Make Palindrome 显示英文描述 
通过的用户数5
尝试过的用户数15
用户总通过次数5
用户总提交次数21
题目难度Hard
You are given a string s consisting only of lowercase English letters.

In one move, you can select any two adjacent characters of s and swap them.

Return the minimum number of moves needed to make s a palindrome.

Note that the input will be generated such that s can always be converted to a palindrome.

 

Example 1:

Input: s = "aabb"
Output: 2
Explanation:
We can obtain two palindromes from s, "abba" and "baab". 
- We can obtain "abba" from s in 2 moves: "aabb" -> "abab" -> "abba".
- We can obtain "baab" from s in 2 moves: "aabb" -> "abab" -> "baab".
Thus, the minimum number of moves needed to make s a palindrome is 2.
Example 2:

Input: s = "letelt"
Output: 2
Explanation:
One of the palindromes we can obtain from s in 2 moves is "lettel".
One of the ways we can obtain it is "letelt" -> "letetl" -> "lettel".
Other palindromes such as "tleelt" can also be obtained in 2 moves.
It can be shown that it is not possible to obtain a palindrome in less than 2 moves.
 

Constraints:

1 <= s.length <= 2000
s consists only of lowercase English letters.
s can be converted to a palindrome using a finite number of moves.

"""


class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        N = len(s)
        jj = N - 1
        res = 0
        while len(s) > 1:
            r = len(s) - 1
            while r and s[r] != s[0]:
                r -= 1
            if r == 0:
                res += len(s) // 2
                s = s[1:]
            else:
                res += len(s) - r - 1
                s = s[1:r] + s[r + 1 :]
        return res
