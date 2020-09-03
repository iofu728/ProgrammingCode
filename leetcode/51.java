/*
 * @Author: gunjianpan
 * @Date:   2020-09-03 09:52:36
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2020-09-03 09:52:38
 */

class Solution {
  char[][] edges;
  List<List<String>> res;
  int[] col;
  int[] diag;
  int[] reverse_diag;
  int N;

  public List<List<String>> solveNQueens(int n) {
    N = n;
    col = new int[N];
    diag = new int[2 * N];
    reverse_diag = new int[2 * N];
    res = new ArrayList<List<String>>();
    edges = new char[N][N];
    for (char[] ii : edges) {
      Arrays.fill(ii, '.');
    }
    dfs(0);
    return res;
  }
  public void dfs(int u) {
    if (u == N) {
      List<String> board = new ArrayList<String>();
      for (int i = 0; i < N; i++) {
        board.add(new String(edges[i]));
      }
      res.add(board);
      return;
    }
    for (int ii = 0; ii < N; ++ii) {
      if (col[ii] == 0 && diag[u + ii] == 0 && reverse_diag[N - u + ii] == 0) {
        edges[u][ii] = 'Q';
        col[ii] = 1;
        diag[u + ii] = 1;
        reverse_diag[N - u + ii] = 1;
        dfs(u + 1);
        edges[u][ii] = '.';
        col[ii] = 0;
        diag[u + ii] = 0;
        reverse_diag[N - u + ii] = 0;
      }
    }
  }
}