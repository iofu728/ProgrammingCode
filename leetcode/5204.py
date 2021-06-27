"""
5204. 统计为蚁群构筑房间的不同顺序 显示英文描述 
通过的用户数138
尝试过的用户数208
用户总通过次数149
用户总提交次数336
题目难度Hard
你是一只蚂蚁，负责为蚁群构筑 n 间编号从 0 到 n-1 的新房间。给你一个 下标从 0 开始 且长度为 n 的整数数组 prevRoom 作为扩建计划。其中，prevRoom[i] 表示在构筑房间 i 之前，你必须先构筑房间 prevRoom[i] ，并且这两个房间必须 直接 相连。房间 0 已经构筑完成，所以 prevRoom[0] = -1 。扩建计划中还有一条硬性要求，在完成所有房间的构筑之后，从房间 0 可以访问到每个房间。

你一次只能构筑 一个 房间。你可以在 已经构筑好的 房间之间自由穿行，只要这些房间是 相连的 。如果房间 prevRoom[i] 已经构筑完成，那么你就可以构筑房间 i。

返回你构筑所有房间的 不同顺序的数目 。由于答案可能很大，请返回对 109 + 7 取余 的结果。

 

示例 1：


输入：prevRoom = [-1,0,1]
输出：1
解释：仅有一种方案可以完成所有房间的构筑：0 → 1 → 2
示例 2：


输入：prevRoom = [-1,0,0,1,2]
输出：6
解释：
有 6 种不同顺序：
0 → 1 → 3 → 2 → 4
0 → 2 → 4 → 1 → 3
0 → 1 → 2 → 3 → 4
0 → 1 → 2 → 4 → 3
0 → 2 → 1 → 3 → 4
0 → 2 → 1 → 4 → 3
 

提示：

n == prevRoom.length
2 <= n <= 105
prevRoom[0] == -1
对于所有的 1 <= i < n ，都有 0 <= prevRoom[i] < n
题目保证所有房间都构筑完成后，从房间 0 可以访问到每个房间
"""


class Solution:
    MOD = 10 ** 9 + 7

    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        N = len(prevRoom)
        # fac[i] 表示 i!
        # inv[i] 表示 i! 的乘法逆元
        F, iF = [0] * N, [0] * N
        F[0] = iF[0] = 1
        for i in range(1, N):
            F[i] = F[i - 1] * i % self.MOD
            # 使用费马小定理计算乘法逆元
            iF[i] = pow(F[i], self.MOD - 2, self.MOD)

        # 构造树
        edges = defaultdict(list)
        for i in range(1, N):
            edges[prevRoom[i]].append(i)

        f, cnt = [0] * N, [0] * N

        def dfs(u: int) -> None:
            f[u] = 1
            for v in edges[u]:
                dfs(v)
                # 乘以左侧的 f[ch] 以及右侧分母中 cnt[ch] 的乘法逆元
                f[u] = f[u] * f[v] * iF[cnt[v]] % self.MOD
                cnt[u] += cnt[v]
            # 乘以右侧分子中的 (cnt[i] - 1)!
            f[u] = f[u] * F[cnt[u]] % self.MOD
            cnt[u] += 1

        dfs(0)
        return f[0]
