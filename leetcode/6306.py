"""
6306. 过桥的时间 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Hard
共有 k 位工人计划将 n 个箱子从旧仓库移动到新仓库。给你两个整数 n 和 k，以及一个二维整数数组 time ，数组的大小为 k x 4 ，其中 time[i] = [leftToRighti, pickOldi, rightToLefti, putNewi] 。

一条河将两座仓库分隔，只能通过一座桥通行。旧仓库位于河的右岸，新仓库在河的左岸。开始时，所有 k 位工人都在桥的左侧等待。为了移动这些箱子，第 i 位工人（下标从 0 开始）可以：

从左岸（新仓库）跨过桥到右岸（旧仓库），用时 leftToRighti 分钟。
从旧仓库选择一个箱子，并返回到桥边，用时 pickOldi 分钟。不同工人可以同时搬起所选的箱子。
从右岸（旧仓库）跨过桥到左岸（新仓库），用时 rightToLefti 分钟。
将箱子放入新仓库，并返回到桥边，用时 putNewi 分钟。不同工人可以同时放下所选的箱子。
如果满足下面任一条件，则认为工人 i 的 效率低于 工人 j ：

leftToRighti + rightToLefti > leftToRightj + rightToLeftj
leftToRighti + rightToLefti == leftToRightj + rightToLeftj 且 i > j
工人通过桥时需要遵循以下规则：

如果工人 x 到达桥边时，工人 y 正在过桥，那么工人 x 需要在桥边等待。
如果没有正在过桥的工人，那么在桥右边等待的工人可以先过桥。如果同时有多个工人在右边等待，那么 效率最低 的工人会先过桥。
如果没有正在过桥的工人，且桥右边也没有在等待的工人，同时旧仓库还剩下至少一个箱子需要搬运，此时在桥左边的工人可以过桥。如果同时有多个工人在左边等待，那么 效率最低 的工人会先过桥。
所有 n 个盒子都需要放入新仓库，请你返回最后一个搬运箱子的工人 到达河左岸 的时间。

 

示例 1：

输入：n = 1, k = 3, time = [[1,1,2,1],[1,1,3,1],[1,1,4,1]]
输出：6
解释：
从 0 到 1 ：工人 2 从左岸过桥到达右岸。
从 1 到 2 ：工人 2 从旧仓库搬起一个箱子。
从 2 到 6 ：工人 2 从右岸过桥到达左岸。
从 6 到 7 ：工人 2 将箱子放入新仓库。
整个过程在 7 分钟后结束。因为问题关注的是最后一个工人到达左岸的时间，所以返回 6 。
示例 2：

输入：n = 3, k = 2, time = [[1,9,1,8],[10,10,10,10]]
输出：50
解释：
从 0 到 10 ：工人 1 从左岸过桥到达右岸。
从 10 到 20 ：工人 1 从旧仓库搬起一个箱子。
从 10 到 11 ：工人 0 从左岸过桥到达右岸。
从 11 到 20 ：工人 0 从旧仓库搬起一个箱子。
从 20 到 30 ：工人 1 从右岸过桥到达左岸。
从 30 到 40 ：工人 1 将箱子放入新仓库。
从 30 到 31 ：工人 0 从右岸过桥到达左岸。
从 31 到 39 ：工人 0 将箱子放入新仓库。
从 39 到 40 ：工人 0 从左岸过桥到达右岸。
从 40 到 49 ：工人 0 从旧仓库搬起一个箱子。
从 49 到 50 ：工人 0 从右岸过桥到达左岸。
从 50 到 58 ：工人 0 将箱子放入新仓库。
整个过程在 58 分钟后结束。因为问题关注的是最后一个工人到达左岸的时间，所以返回 50 。
 

提示：

1 <= n, k <= 104
time.length == k
time[i].length == 4
1 <= leftToRighti, pickOldi, rightToLefti, putNewi <= 1000
"""
class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        frees, right, left = [], [], []
        times = 0
        res = 0
        for ii, jj in enumerate(time):
            heapq.heappush(frees, (-(jj[0] + jj[2]), -ii))
        z = 0
        # print(frees)
        while z < n:
            ys = []
            while right:
                y = heapq.heappop(right)
                if y[0] <= times:
                    heapq.heappush(ys, (-(time[y[1]][0] + time[y[1]][2]), -y[1]))
                else:
                    heapq.heappush(right, y)
                    break
            empty = len(ys) == 0
            # print(ys, times)
            if ys:
                y = heapq.heappop(ys)
                y_ids = -y[1]
                times += time[y_ids][2]
                res = times
                # print(res)
                heapq.heappush(left, (times + time[y_ids][3], y_ids))
                while ys:
                    y = heapq.heappop(ys)
                    heapq.heappush(right, (times, -y[1]))
            if right:
                y = heapq.heappop(right)
                heapq.heappush(right, y)
                if y[0] <= times:
                    continue
            while left:
                x = heapq.heappop(left)
                if x[0] <= times:
                    heapq.heappush(frees, (-(time[x[1]][0] + time[x[1]][2]), -x[1]))
                else:
                    heapq.heappush(left, x)
                    break
            # print("frees", frees, times)
            if frees:
                x = heapq.heappop(frees)
                x_ids = -x[1]
                times += time[x_ids][0]
                heapq.heappush(right, (times + time[x_ids][1], x_ids))
                z += 1
                # print("-", times)
            elif empty:
                # print(frees, left, right, times)
                if not right:
                    a = heapq.heappop(left)
                    times = a[0]
                    heapq.heappush(left, a)
                elif not left:
                    b = heapq.heappop(right)
                    times = b[0]
                    heapq.heappush(right, b)
                else:
                    b = heapq.heappop(right)
                    a = heapq.heappop(left)
                    if b[0] <= a[0]:
                        times = b[0]
                    else:
                        times = a[0]
                    heapq.heappush(left, a)
                    heapq.heappush(right, b)
        
        while right:
            ys = []
            # print("+", right)
            while right:
                y = heapq.heappop(right)
                if y[0] <= times:
                    heapq.heappush(ys, (-(time[y[1]][0] + time[y[1]][2]), -y[1]))
                else:
                    heapq.heappush(right, y)
                    break
            empty = len(ys) == 0
            # print(ys)
            if ys:
                y = heapq.heappop(ys)
                y_ids = -y[1]
                times += time[y_ids][2]
                res = times
                # print(res)
                heapq.heappush(left, (times + time[y_ids][3], y_ids))
                while ys:
                    y = heapq.heappop(ys)
                    heapq.heappush(right, (times, -y[1]))
            if empty:

                b = heapq.heappop(right)
                times = b[0]
                heapq.heappush(right, b)

        return res

            
            
        
        