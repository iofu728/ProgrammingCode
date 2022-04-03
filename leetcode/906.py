# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-04-02 15:14:03
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-04-02 15:14:14

"""
906. 超级回文数
如果一个正整数自身是回文数，而且它也是一个回文数的平方，那么我们称这个数为超级回文数。

现在，给定两个正整数 L 和 R （以字符串形式表示），返回包含在范围 [L, R] 中的超级回文数的数目。

 

示例：

输入：L = "4", R = "1000"
输出：4
解释：
4，9，121，以及 484 是超级回文数。
注意 676 不是一个超级回文数： 26 * 26 = 676，但是 26 不是回文数。
 

提示：

1 <= len(L) <= 18
1 <= len(R) <= 18
L 和 R 是表示 [1, 10^18) 范围的整数的字符串。
int(L) <= int(R)
 

通过次数2,661提交次数9,057
"""
class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        def is_ok(a):
            a = str(a)
            l, r = 0, len(a) - 1
            while l < r:
                if a[l] != a[r]:
                    return False
                l += 1
                r -= 1
            return True

        L, R = int(left), int(right)
        MAGIC = 10 ** 5
        res = 0
        for ii in range(MAGIC):
            s = str(ii) + str(ii)[::-1]
            k = int(s) ** 2
            if k > R:
                break
            if k >= L and is_ok(k):
                res += 1
        for ii in range(MAGIC):
            s = str(ii) + str(ii)[-2::-1]
            k = int(s) ** 2
            if k > R:
                break
            if k >= L and is_ok(k):
                res += 1
        return res
