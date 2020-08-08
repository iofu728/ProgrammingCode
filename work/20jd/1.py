import sys

N = int(sys.stdin.readline())
T = sys.stdin.readline().strip().split()
D = sys.stdin.readline().strip().split()


def get_max_sim():
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for ii in range(N):
        for jj in range(N):
            if T[ii] == D[jj]:
                dp[ii + 1][jj + 1] = dp[ii][jj] + 1
            else:
                dp[ii + 1][jj + 1] = max(dp[ii][jj + 1], dp[ii + 1][jj])
    MAX = dp[N][N]
    res = MAX / N
    return "{:.2f} {}".format(res, "Yes" if res <= 0.5 else "No")


print(get_max_sim())
