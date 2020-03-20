/*
 * @Author: gunjianpan
 * @Date:   2018-09-15 16:54:47
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2018-09-15 19:36:07
 */
#include <iostream>
#include <queue>

using namespace std;

struct node {
  int x, y, z;
};

const int MAXNX = 1300;
const int MAXNY = 130;
const int MAXNZ = 70;
int X[6] = {1, 0, 0, -1, 0, 0};
int Y[6] = {0, 1, 0, 0, -1, 0};
int Z[6] = {0, 0, 1, 0, 0, -1};

int n, m, l, t, totalblock = 0, matrix[MAXNX][MAXNY][MAXNZ];
bool vis[MAXNX][MAXNY][MAXNZ] = {false};

bool judge(int x, int y, int z) {
  if (x >= n || x < 0 || y >= m || y < 0 || z >= l || z < 0) return false;
  if (matrix[x][y][z] != 1 || vis[x][y][z]) return false;
  return true;
}

int bfs(int x, int y, int z) {
  int block = 0;
  queue<node> q;
  node start = {x, y, z};
  q.push(start);
  vis[x][y][z] = true;
  while (!q.empty()) {
    node top = q.front();
    q.pop();
    ++block;
    for (int i = 0; i < 6; ++i) {
      int newX = top.x + X[i];
      int newY = top.y + Y[i];
      int newZ = top.z + Z[i];
      if (judge(newX, newY, newZ)) {
        node next = {newX, newY, newZ};
        q.push(next);
        vis[newX][newY][newZ] = true;
      }
    }
  }
  return block;
}

int main(int argc, char const *argv[]) {
  cin >> n >> m >> l >> t;
  for (int i = 0; i < l; ++i)
    for (int j = 0; j < n; ++j)
      for (int k = 0; k < m; ++k) cin >> matrix[j][k][i];
  for (int i = 0; i < n; ++i)
    for (int j = 0; j < m; ++j)
      for (int k = 0; k < l; ++k) {
        if (!vis[i][j][k] && matrix[i][j][k] == 1) {
          int tempblock = bfs(i, j, k);
          if (tempblock >= t) totalblock += tempblock;
        }
      }
  cout << totalblock;

  return 0;
}
