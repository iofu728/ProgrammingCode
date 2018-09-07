#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;

const int maxn = 10001;
const int inf = 0x3fffffff;
struct node {
  int u, v;
};
vector<node> G;
int n, m, k;
int hashh[maxn];
bool vis;
int main() {
  scanf("%d%d", &n, &m);
  for (int i = 0; i < m; i++) {
    node temp;
    int u, v;
    scanf("%d %d", &u, &v);
    temp.u = u;
    temp.v = v;
    G.push_back(temp);
  }
  scanf("%d", &k);
  for (int i = 0; i < k; i++) {
    fill(hashh, hashh + maxn, inf);
    vis = true;
    int g, f;
    scanf("%d", &g);
    for (int j = 0; j < g; j++) {
      scanf("%d", &f);
      hashh[f] = 0;
    }
    for (int j = 0; j < m; j++) {
      node nowg = G[j];
      if (hashh[nowg.u] != 0 && hashh[nowg.v] != 0) vis = false;
    }
    if (vis == false)
      printf("No\n");
    else
      printf("Yes\n");
  }

  return 0;
}
