# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-04-14 13:00:10
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-04-14 13:00:28

"""
100259. 划分数组得到最小的值之和 显示英文描述 
通过的用户数108
尝试过的用户数416
用户总通过次数139
用户总提交次数1210
题目难度Hard
给你两个数组 nums 和 andValues，长度分别为 n 和 m。

数组的 值 等于该数组的 最后一个 元素。

你需要将 nums 划分为 m 个 不相交的连续 子数组，对于第 ith 个子数组 [li, ri]，子数组元素的按位AND运算结果等于 andValues[i]，换句话说，对所有的 1 <= i <= m，nums[li] & nums[li + 1] & ... & nums[ri] == andValues[i] ，其中 & 表示按位AND运算符。

返回将 nums 划分为 m 个子数组所能得到的可能的 最小 子数组 值 之和。如果无法完成这样的划分，则返回 -1 。

 

示例 1：

输入： nums = [1,4,3,3,2], andValues = [0,3,3,2]

输出： 12

解释：

唯一可能的划分方法为：

[1,4] 因为 1 & 4 == 0
[3] 因为单元素子数组的按位 AND 结果就是该元素本身
[3] 因为单元素子数组的按位 AND 结果就是该元素本身
[2] 因为单元素子数组的按位 AND 结果就是该元素本身
这些子数组的值之和为 4 + 3 + 3 + 2 = 12

示例 2：

输入： nums = [2,3,5,7,7,7,5], andValues = [0,7,5]

输出： 17

解释：

划分 nums 的三种方式为：

[[2,3,5],[7,7,7],[5]] 其中子数组的值之和为 5 + 7 + 5 = 17
[[2,3,5,7],[7,7],[5]] 其中子数组的值之和为 7 + 7 + 5 = 19
[[2,3,5,7,7],[7],[5]] 其中子数组的值之和为 7 + 7 + 5 = 19
子数组值之和的最小可能值为 17

示例 3：

输入： nums = [1,2,3,4], andValues = [2]

输出： -1

解释：

整个数组 nums 的按位 AND 结果为 0。由于无法将 nums 划分为单个子数组使得元素的按位 AND 结果为 2，因此返回 -1。

 

提示：

1 <= n == nums.length <= 104
1 <= m == andValues.length <= min(n, 10)
1 <= nums[i] < 105
0 <= andValues[j] < 105
"""
import typing

class SparseTable:
    def __init__(self, data, merge_method):
        self.note = [0] * (len(data) + 1)
        self.merge_method = merge_method
        l, r, v = 1, 2, 0
        while True:
            for i in range(l, r):
                if i >= len(self.note):
                    break
                self.note[i] = v
            else:
                l *= 2
                r *= 2
                v += 1
                continue
            break
        self.ST = [[0] * len(data) for _ in range(self.note[-1]+1)]
        self.ST[0] = data
        for i in range(1, len(self.ST)):
            for j in range(len(data) - (1 << i) + 1):
                self.ST[i][j] = merge_method(self.ST[i-1][j], self.ST[i-1][j + (1 << (i-1))])

    def query(self, l, r):
        pos = self.note[r-l+1]
        return self.merge_method(self.ST[pos][l], self.ST[pos][r - (1 << pos) + 1])

class SegTree:
    def __init__(self,
                 op: typing.Callable[[typing.Any, typing.Any], typing.Any],
                 e: typing.Any,
                 v: typing.Union[int, typing.List[typing.Any]]) -> None:
        self._op = op
        self._e = e

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = (self._n - 1).bit_length()
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)

        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def set(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += self._size
        if x < self._d[p]:
            self._d[p] = x
            for i in range(1, self._log + 1):
                self._update(p >> i)

    def get(self, p: int) -> typing.Any:
        assert 0 <= p < self._n

        return self._d[p + self._size]

    def prod(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n
        sml = self._e
        smr = self._e
        left += self._size
        right += self._size

        while left < right:
            if left & 1:
                sml = self._op(sml, self._d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self._op(self._d[right], smr)
            left >>= 1
            right >>= 1

        return self._op(sml, smr)

    def all_prod(self) -> typing.Any:
        return self._d[1]

    def max_right(self, left: int,
                  f: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= left <= self._n
        assert f(self._e)

        if left == self._n:
            return self._n

        left += self._size
        sm = self._e

        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not f(self._op(sm, self._d[left])):
                while left < self._size:
                    left *= 2
                    if f(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    def min_left(self, right: int,
                 f: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= right <= self._n
        assert f(self._e)

        if right == 0:
            return 0

        right += self._size
        sm = self._e

        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not f(self._op(self._d[right], sm)):
                while right < self._size:
                    right = 2 * right + 1
                    if f(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self._d[right], sm)

        return 0

    def _update(self, k: int) -> None:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

inf = 10 ** 7
class Solution:
    def minimumValueSum(self, nums: List[int], vals: List[int]) -> int:
        st = SparseTable(nums, iand)
        n = len(nums)
        m = len(vals)
        
        dp = [SegTree(min, inf, n + 1) for _ in range(m + 1)]
        dp[0].set(0, 0)
        
        for i in range(n):
            for j in range(m):
                l, r = 0, i
                while l <= r:
                    mid = (l + r) // 2
                    if st.query(mid, i) > vals[j]:
                        r = mid - 1
                    else:
                        l = mid + 1
                right = r
                l, r = 0, i
                while l <= r:
                    mid = (l + r) // 2
                    if st.query(mid, i) < vals[j]:
                        l = mid + 1
                    else:
                        r = mid - 1
                left = l
                if left > right: continue
                dp[j + 1].set(i + 1, dp[j].prod(left, right + 1) + nums[i])
        ans = dp[m].get(n)
        return ans if ans < inf else -1
