# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-07-02 11:22:36
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-07-02 11:22:45

"""
6916. 和等于目标值的质数对 显示英文描述 
通过的用户数432
尝试过的用户数638
用户总通过次数434
用户总提交次数951
题目难度Medium
给你一个整数 n 。如果两个整数 x 和 y 满足下述条件，则认为二者形成一个质数对：

1 <= x <= y <= n
x + y == n
x 和 y 都是质数
请你以二维有序列表的形式返回符合题目要求的所有 [xi, yi] ，列表需要按 xi 的 非递减顺序 排序。如果不存在符合要求的质数对，则返回一个空数组。

注意：质数是大于 1 的自然数，并且只有两个因子，即它本身和 1 。

 

示例 1：

输入：n = 10
输出：[[3,7],[5,5]]
解释：在这个例子中，存在满足条件的两个质数对。 
这两个质数对分别是 [3,7] 和 [5,5]，按照题面描述中的方式排序后返回。
示例 2：

输入：n = 2
输出：[]
解释：可以证明不存在和为 2 的质数对，所以返回一个空数组。 
 

提示：

1 <= n <= 106
"""
def euler_flag_prime(n):
    # 欧拉线性筛素数
    # 说明：返回小于等于 n 的所有素数
    flag = [False for _ in range(n + 1)]
    prime_numbers = []
    for num in range(2, n + 1):
        if not flag[num]:
            prime_numbers.append(num)
        for prime in prime_numbers:
            if num * prime > n:
                break
            flag[num * prime] = True
            if num % prime == 0:  # 这句是最有意思的地方  下面解释
                break
    return prime_numbers

y = set(euler_flag_prime(10 ** 6))

class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        res = []
        for ii in range(2, n // 2 + 10):
            if ii in y and n - ii in y and ii <= n - ii:
                res.append([ii, n - ii])
        return res
        