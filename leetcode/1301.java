/*
 * @Author: gunjianpan
 * @Date:   2020-09-03 12:12:23
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2020-09-03 12:12:26
 */

class Solution {
  int MODS = 1000000007;
  int[][] dpScore;
  int[][] dpNum;
  int n;

  public int[] pathsWithMaxScore(List<String> board) {
    n = board.size();
    dpScore = new int[n][n];
    dpNum = new int[n][n];
    for (int[] ii : dpScore) {
      Arrays.fill(ii, -1);
    }
    dpScore[n - 1][n - 1] = 0;
    dpNum[n - 1][n - 1] = 1;
    for (int i = n - 1; i >= 0; --i) {
      for (int j = n - 1; j >= 0; --j) {
        if (i == n - 1 && j == n - 1) {
          continue;
        }
        if (board.get(i).charAt(j) != 'X') {
          update(i, j, i + 1, j);
          update(i, j, i, j + 1);
          update(i, j, i + 1, j + 1);
          if (dpScore[i][j] != -1) {
            dpScore[i][j] += ((board.get(i).charAt(j) == 'E'
                                   ? 0
                                   : (board.get(i).charAt(j) - '0')));
          }
        }
      }
    }
    if (dpScore[0][0] == -1) {
      return new int[] {0, 0};
    }
    return new int[] {dpScore[0][0], dpNum[0][0] % MODS};
  }
  public void update(int x, int y, int u, int v) {
    if (u >= n || v >= n || dpScore[u][v] == -1) {
      return;
    }
    if (dpScore[u][v] > dpScore[x][y]) {
      dpScore[x][y] = dpScore[u][v];
      dpNum[x][y] = dpNum[u][v];
    } else if (dpScore[u][v] == dpScore[x][y]) {
      dpNum[x][y] = (dpNum[x][y] + dpNum[u][v]) % MODS;
    }
  }
}
