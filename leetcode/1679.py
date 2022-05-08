"""
1679. K 和数对的最大数目
给你一个整数数组 nums 和一个整数 k 。

每一步操作中，你需要从数组中选出和为 k 的两个整数，并将它们移出数组。

返回你可以对数组执行的最大操作数。

 

示例 1：

输入：nums = [1,2,3,4], k = 5
输出：2
解释：开始时 nums = [1,2,3,4]：
- 移出 1 和 4 ，之后 nums = [2,3]
- 移出 2 和 3 ，之后 nums = []
不再有和为 5 的数对，因此最多执行 2 次操作。
示例 2：

输入：nums = [3,1,3,4,3], k = 6
输出：1
解释：开始时 nums = [3,1,3,4,3]：
- 移出前两个 3 ，之后nums = [1,4,3]
不再有和为 6 的数对，因此最多执行 1 次操作。
 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109
通过次数8,298提交次数16,343
"""
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        res = 0
        for x, xx in c.items():
            y = k - x
            if y < x:
                continue
            yy = c.get(y, 0)
            if x == y:
                res += xx // 2
            else:
                res += min(xx, yy)
        return res
            
            

