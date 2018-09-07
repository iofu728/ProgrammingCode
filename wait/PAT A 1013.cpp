#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

const int maxn = 1111;

vector<int> G[maxn];
bool vis[maxn];
int currentpoint;

void dfs(int v) {
  if (v == currentpoint) return;
  vis[v] = true;
  for (int i = 0; i < G[v].size(); i++) {
    if (vis[G[v][i]] == false) {
      dfs(G[v][i]);
    }
  }
}
int n, m, k;
int main() {
  scanf("%d %d %d", &n, &m, &k);
  for (int i = 0; i < m; i++) {
    int a, b;
    scanf("%d %d", &a, &b);
    G[a].push_back(b);
    G[b].push_back(a);
  }
  for (int j = 0; j < k; j++) {
    scanf("%d", &currentpoint);
    memset(vis, false, sizeof(vis));
    int block = 0;
    for (int i = 1; i <= n; i++) {
      if (i != currentpoint && vis[i] == false) {
        dfs(i);
        block++;
      }
    }
    printf("%d\n", block - 1);
  }
  return 0;
}
