"""
100600. 将水果放入篮子 II 显示英文描述 
通过的用户数9
尝试过的用户数12
用户总通过次数9
用户总提交次数12
题目难度Easy
给你两个长度为 n 的整数数组，fruits 和 baskets，其中 fruits[i] 表示第 i 种水果的 数量，baskets[j] 表示第 j 个篮子的 容量。

你需要对 fruits 数组从左到右按照以下规则放置水果：

每种水果必须放入第一个 容量大于等于 该水果数量的 最左侧可用篮子 中。
每个篮子只能装 一种 水果。
如果一种水果 无法放入 任何篮子，它将保持 未放置。
返回所有可能分配完成后，剩余未放置的水果种类的数量。

 

示例 1

输入： fruits = [4,2,5], baskets = [3,5,4]

输出： 1

解释：

fruits[0] = 4 放入 baskets[1] = 5。
fruits[1] = 2 放入 baskets[0] = 3。
fruits[2] = 5 无法放入 baskets[2] = 4。
由于有一种水果未放置，我们返回 1。

示例 2

输入： fruits = [3,6,1], baskets = [6,4,7]

输出： 0

解释：

fruits[0] = 3 放入 baskets[0] = 6。
fruits[1] = 6 无法放入 baskets[1] = 4（容量不足），但可以放入下一个可用的篮子 baskets[2] = 7。
fruits[2] = 1 放入 baskets[1] = 4。
由于所有水果都已成功放置，我们返回 0。

 

提示：

n == fruits.length == baskets.length
1 <= n <= 100
1 <= fruits[i], baskets[i] <= 1000

"""
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        res = 0
        done = set()
        for x in fruits:
            flag = False
            for i, j in enumerate(baskets):
                if j >= x and i not in done:
                    done.add(i)
                    flag = True
                    break
            if flag is False:
                res += 1
        return res
        