#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;

const int INF = 0x3fffffff;
const int maxn = 500;
int n, G[maxn][maxn];
int d[maxn], w[maxn], num[maxn], weight[maxn];
bool vis[maxn] = {false};

void Dijkstra(int s) {
  fill(d, d + maxn, INF);
  memset(num, 0, sizeof(num));
  memset(w, 0, sizeof(w));
  d[s] = 0;
  num[s] = 1;
  w[s] = weight[s];
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
          num[v] = num[u];
          w[v] = weight[v] + w[u];
        } else if (d[u] + G[u][v] == d[v]) {
          if (weight[v] + w[u] > w[v]) w[v] = weight[v] + w[u];
          num[v] += num[u];
        }
      }
    }
  }
}

int main() {
  int m, c1, c2;
  scanf("%d%d%d%d", &n, &m, &c1, &c2);
  for (int i = 0; i < n; i++) {
    scanf("%d", &weight[i]);
  }
  int u, v;
  fill(G[0], G[0] + maxn * maxn, INF);
  for (int i = 0; i < m; i++) {
    scanf("%d", &u);
    scanf("%d", &v);
    scanf("%d", &G[u][v]);
    G[v][u] = G[u][v];
  }
  Dijkstra(c1);
  printf("%d %d", num[c2], w[c2]);
  return 0;
}
