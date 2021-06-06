"""
5776. 判断矩阵经轮转后是否一致 显示英文描述 
通过的用户数2705
尝试过的用户数2935
用户总通过次数2755
用户总提交次数5101
题目难度Easy
给你两个大小为 n x n 的二进制矩阵 mat 和 target 。现 以 90 度顺时针轮转 矩阵 mat 中的元素 若干次 ，如果能够使 mat 与 target 一致，返回 true ；否则，返回 false 。

 

示例 1：


输入：mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
输出：true
解释：顺时针轮转 90 度一次可以使 mat 和 target 一致。
示例 2：


输入：mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
输出：false
解释：无法通过轮转矩阵中的元素使 equal 与 target 一致。
示例 3：


输入：mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
输出：true
解释：顺时针轮转 90 度两次可以使 mat 和 target 一致。
 

提示：

n == mat.length == target.length
n == mat[i].length == target[i].length
1 <= n <= 10
mat[i][j] 和 target[i][j] 不是 0 就是 1
"""


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def change(matrix):
            n = len(matrix)
            # 水平翻转
            for i in range(n // 2):
                for j in range(n):
                    matrix[i][j], matrix[n - i - 1][j] = (
                        matrix[n - i - 1][j],
                        matrix[i][j],
                    )
            # 主对角线翻转
            for i in range(n):
                for j in range(i):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            return matrix

        if mat == target:
            return True
        for ii in range(3):
            mat = change(mat)
            if mat == target:
                return True
        return False