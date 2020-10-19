
    def totalNQueens(self, n: int) -> int:
        def dfs(pre: list, line1: list, line2: list):
            nonlocal res
            # print(pre, line1, line2)
            if not pre:
                res += 1
                return
            for ii, jj in enumerate(pre):
                x, y = n - len(pre) + jj, n - len(pre) - jj + n
                # print(x, y)
                if line1[x] == 0 and line2[y] == 0:
                    line1[x] = 1
                    line2[y] = 1
                    dfs(pre[:ii] + pre[ii + 1:], line1, line2)
                    line1[x] = 0
                    line2[y] = 0
        res = 0
        dfs(list(range(n)), [0] * 2 * n, [0] * 2 * n)
        return res