"""
100563. 距离最小相等元素查询 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个 循环 数组 nums 和一个数组 queries 。

对于每个查询 i ，你需要找到以下内容：

数组 nums 中下标 queries[i] 处的元素与 任意 其他下标 j（满足 nums[j] == nums[queries[i]]）之间的 最小 距离。如果不存在这样的下标 j，则该查询的结果为 -1 。
返回一个数组 answer，其大小与 queries 相同，其中 answer[i] 表示查询i的结果。

 

示例 1：

输入： nums = [1,3,1,4,1,3,2], queries = [0,3,5]

输出： [2,-1,3]

解释：

查询 0：下标 queries[0] = 0 处的元素为 nums[0] = 1 。最近的相同值下标为 2，距离为 2。
查询 1：下标 queries[1] = 3 处的元素为 nums[3] = 4 。不存在其他包含值 4 的下标，因此结果为 -1。
查询 2：下标 queries[2] = 5 处的元素为 nums[5] = 3 。最近的相同值下标为 1，距离为 3（沿着循环路径：5 -> 6 -> 0 -> 1）。
示例 2：

输入： nums = [1,2,3,4], queries = [0,1,2,3]

输出： [-1,-1,-1,-1]

解释：

数组 nums 中的每个值都是唯一的，因此没有下标与查询的元素值相同。所有查询的结果均为 -1。

 

提示：

1 <= queries.length <= nums.length <= 105
1 <= nums[i] <= 106
0 <= queries[i] < nums.length
"""
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        def get_d(x, y):
            if len(c[x]) == 1:
                return -1
            idx = bisect.bisect_left(c[x], y)
            left = (idx - 1 + len(c[x])) % len(c[x])
            right = (idx + 1) % len(c[x])
            left = (c[x][idx] + n - c[x][left]) % n
            right = (c[x][right] + n - c[x][idx]) % n
            return min(left, right)
            
        n = len(nums)
        c = defaultdict(list)
        for i, j in enumerate(nums):
            c[j].append(i)
        res = []
        for i in queries:
            res.append(get_d(nums[i], i))
        return res
        
        