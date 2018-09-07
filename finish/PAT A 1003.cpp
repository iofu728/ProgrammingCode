#include <algorithm>
#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

const int INF = 0x3fffffff;
const int maxn = 510;
int n, m, c1, c2, G[maxn][maxn], mincost = INF;
int d[maxn], c[maxn], num[maxn], cost[maxn][maxn];
bool vis[maxn] = {false};
vector<int> pre[maxn];
vector<int> tempath, path;

void Dijkstra(int s) {
  fill(d, d + maxn, INF);
  memset(num, 0, sizeof(num));
  d[s] = 0;
  num[s] = 1;
  for (int i = 0; i < n; i++) {
    int u = -1, MIN = INF;
    for (int j = 0; j < n; j++) {
      if (vis[j] == false && d[j] < MIN) {
        u = j;
        MIN = d[j];
      }
    }
    if (u == -1) return;
    vis[u] = true;
    for (int v = 0; v < n; v++) {
      if (vis[v] == false && G[u][v] != INF) {
        if (d[u] + G[u][v] < d[v]) {
          d[v] = d[u] + G[u][v];
          pre[v].clear();
          pre[v].push_back(u);
        } else if (d[u] + G[u][v] == d[v]) {
          pre[v].push_back(u);
        }
      }
    }
  }
}
void DFS(int v) {
  if (v == c1) {
    tempath.push_back(v);
    int temcost = 0;
    for (int i = tempath.size() - 1; i > 0; i--) {
      int id = tempath[i], idnext = tempath[i - 1];
      temcost += cost[id][idnext];
    }
    if (temcost < mincost) {
      mincost = temcost;
      path = tempath;
    }
    tempath.pop_back();
    return;
  }
  tempath.push_back(v);
  for (int i = 0; i < pre[v].size(); i++) {
    DFS(pre[v][i]);
  }
  tempath.pop_back();
}

int main() {
  scanf("%d%d%d%d", &n, &m, &c1, &c2);

  int u, v;
  fill(G[0], G[0] + maxn * maxn, INF);
  fill(cost[0], cost[0] + maxn * maxn, INF);
  for (int i = 0; i < m; i++) {
    scanf("%d", &u);
    scanf("%d", &v);
    scanf("%d", &G[u][v], &cost[u][v]);
    G[v][u] = G[u][v];
    cost[v][u] = cost[u][v];
  }
  Dijkstra(c1);
  DFS(c2);
  for (int i = path.size(); i >= 0; i--) {
    printf("%d ", path[i]);
  }
  printf("%d %d\n", d[c2], mincost);
  return 0;
}
