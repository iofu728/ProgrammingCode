"""
100572. 将元素分配给有约束条件的组 显示英文描述 
通过的用户数34
尝试过的用户数86
用户总通过次数34
用户总提交次数106
题目难度Medium
给你一个整数数组 groups，其中 groups[i] 表示第 i 组的大小。另给你一个整数数组 elements。

请你根据以下规则为每个组分配 一个 元素：

如果 groups[i] 能被 elements[j] 整除，则元素 j 可以分配给组 i。
如果有多个元素满足条件，则分配下标最小的元素  j 。
如果没有元素满足条件，则分配 -1 。
返回一个整数数组 assigned，其中 assigned[i] 是分配给组 i 的元素的索引，若无合适的元素，则为 -1。

注意：一个元素可以分配给多个组。

 

示例 1：

输入： groups = [8,4,3,2,4], elements = [4,2]

输出： [0,0,-1,1,0]

解释：

elements[0] = 4 被分配给组 0、1 和 4。
elements[1] = 2 被分配给组 3。
无法为组 2 分配任何元素，分配 -1 。
示例 2：

输入： groups = [2,3,5,7], elements = [5,3,3]

输出： [-1,1,0,-1]

解释：

elements[1] = 3 被分配给组 1。
elements[0] = 5 被分配给组 2。
无法为组 0 和组 3 分配任何元素，分配 -1 。
示例 3：

输入： groups = [10,21,30,41], elements = [2,1]

输出： [0,1,0,1]

解释：

elements[0] = 2 被分配给所有偶数值的组，而 elements[1] = 1 被分配给所有奇数值的组。

 

提示：

1 <= groups.length <= 105
1 <= elements.length <= 105
1 <= groups[i] <= 105
1 <= elements[i] <= 105

"""

class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        g = {}
        for i, j in enumerate(elements):
            if j not in g:
                g[j] = i
        g_max = max(groups)
        
        res = []
        for now in groups:
            factors = set()
            for i in range(1, math.isqrt(now) + 1):
                if now % i == 0:
                    factors.add(i)
                    factors.add(now // i)
            min_idx = float('inf')
            for d in factors:
                if d in g:
                    if g[d] < min_idx:
                        min_idx = g[d]
            if min_idx != float('inf'):
                res.append(min_idx)
            else:
                res.append(-1)
        return res
        