# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-15 10:42:52
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-15 10:53:59


"""
5356. Lucky Numbers in a Matrix
User Accepted:3094
User Tried:3287
Total Accepted:3117
Total Submissions:3757
Difficulty:Easy
Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

 

Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column
Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 3:

Input: matrix = [[7,8],[1,2]]
Output: [7]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= n, m <= 50
1 <= matrix[i][j] <= 10^5.
All elements in the matrix are distinct.
"""


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        def is_max(x: int, y: int) -> bool:
            for ii in matrix:
                if matrix[x][y] < ii[y]:
                    return False
            return True

        max_indexs = [sorted(enumerate(ii), key=lambda i: i[1])[0][0] for ii in matrix]
        return [matrix[x][y] for x, y in enumerate(max_indexs) if is_max(x, y)]
