# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-10-24 11:58:46
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-10-24 11:58:58

"""
5907. 下一个更大的数值平衡数 显示英文描述 
通过的用户数207
尝试过的用户数248
用户总通过次数208
用户总提交次数328
题目难度Medium
如果整数  x 满足：对于每个数位 d ，这个数位 恰好 在 x 中出现 d 次。那么整数 x 就是一个 数值平衡数 。

给你一个整数 n ，请你返回 严格大于 n 的 最小数值平衡数 。

 

示例 1：

输入：n = 1
输出：22
解释：
22 是一个数值平衡数，因为：
- 数字 2 出现 2 次 
这也是严格大于 1 的最小数值平衡数。
示例 2：

输入：n = 1000
输出：1333
解释：
1333 是一个数值平衡数，因为：
- 数字 1 出现 1 次。
- 数字 3 出现 3 次。 
这也是严格大于 1000 的最小数值平衡数。
注意，1022 不能作为本输入的答案，因为数字 0 的出现次数超过了 0 。
示例 3：

输入：n = 3000
输出：3133
解释：
3133 是一个数值平衡数，因为：
- 数字 1 出现 1 次。
- 数字 3 出现 3 次。 
这也是严格大于 3000 的最小数值平衡数。
 

提示：

0 <= n <= 106
"""
from itertools import permutations


class Solution:
    q = [1, 2, 3, 4, 5, 6]

    def nextBeautifulNumber(self, n: int) -> int:
        def dfs(idx, now, is_update=False):
            if len(now) > 7 or idx > 7:
                return
            # print(now)
            if is_update:
                self.res.update(
                    set(
                        [int("".join([str(k) for k in kk])) for kk in permutations(now)]
                    )
                )
            dfs(idx + 1, now + [idx] * idx, True)
            dfs(idx + 1, now)

        self.res = set()
        dfs(1, [])
        return min([ii for ii in self.res if ii > n])
