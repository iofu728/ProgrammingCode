"""
3566. 等积子集的划分方案
已解答
中等
premium lock icon
相关企业
提示
给你一个整数数组 nums，其中包含的正整数 互不相同 ，另给你一个整数 target。

请判断是否可以将 nums 分成两个 非空、互不相交 的 子集 ，并且每个元素必须  恰好 属于 一个 子集，使得这两个子集中元素的乘积都等于 target。

如果存在这样的划分，返回 true；否则，返回 false。

子集 是数组中元素的一个选择集合。

 

示例 1：

输入： nums = [3,1,6,8,4], target = 24

输出： true

解释：子集 [3, 8] 和 [1, 6, 4] 的乘积均为 24。因此，输出为 true 。

示例 2：

输入： nums = [2,5,3,7], target = 15

输出： false

解释：无法将 nums 划分为两个非空的互不相交子集，使得它们的乘积均为 15。因此，输出为 false。

 

提示：

3 <= nums.length <= 12
1 <= target <= 1015
1 <= nums[i] <= 100
nums 中的所有元素互不相同。
"""
class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        def dfs(x, y):
            if x >= N:
                return False
            if self.res:
                return True
            res = False
            if y % nums[x] == 0:
                if y == nums[x]:
                    self.res = True
                    return True
                res = dfs(x + 1, y // nums[x])
            res = res | dfs(x + 1, y)
            return res
            
            
        c = Counter(nums)
        N = len(nums)
        self.res = False
        y = 1
        for i in nums:
            y = y * i
        if y != target ** 2:
            return False
        dfs(0, target)
        return self.res
        