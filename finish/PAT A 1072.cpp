#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
const int INF = 0x3fffffff;
const int maxn = 1020;
int n, m, k, dg, maxd, ansid;
double avar, mind, ansdis, ansavar;
int G[maxn][maxn], d[maxn];
bool vis[maxn];

void Dijkstra(int start) {
  fill(d, d + maxn, INF);
  fill(vis, vis + maxn, false);
  d[start] = 0;
  for (int i = 1; i <= n + m; ++i) {
    int u = -1, MIN = INF;
    for (int j = 1; j <= n + m; ++j) {
      if (!vis[j] && d[j] < MIN) {
        u = j;
        MIN = d[j];
      }
    }
    if (u == -1) break;
    vis[u] = true;
    for (int v = 1; v <= n + m; ++v) {
      if (!vis[v] && G[u][v] != INF && d[u] + G[u][v] < d[v]) {
        d[v] = d[u] + G[u][v];
      }
    }
  }
  double sum = 0, num = 0;
  mind = INF, maxd = -1;
  for (int i = 1; i <= n; ++i) {
    if (d[i] > dg) {
      mind = -1;
      return;
    }
    if (d[i] < mind) {
      mind = d[i];
    }
    if (d[i] != INF) {
      sum += d[i] * 1.0;
      ++num;
    }
    //		cout<<d[i]<<' ';
  }
  //	cout<<sum<<' '<<num<<endl;
  avar = sum / num * 1.0;
  return;
}

int stringnum(string str) {
  if (str[0] == 'G') {
    return (str[1] - '0') + n;
  } else
    return str[0] - '0';
}
int main() {
  cin >> n >> m >> k >> dg;
  getchar();
  fill(G[0], G[0] + maxn * maxn, INF);
  for (int i = 0; i < k; ++i) {
    int id1, id2;
    string str1, str2;
    cin >> str1 >> str2;
    id1 = stringnum(str1);
    id2 = stringnum(str2);
    cin >> G[id1][id2];
    G[id2][id1] = G[id1][id2];
    getchar();
  }
  for (int i = n + 1; i <= n + m; ++i) {
    Dijkstra(i);
    if (mind == -1) continue;
    if (mind > ansdis) {
      ansid = i;
      ansdis = mind;
      ansavar = avar;
    } else if (mind == ansdis && avar < ansavar) {
      ansid = i;
      ansavar = avar;
    }
  }
  if (ansid == -1) {
    cout << "No Solution\n";
  } else {
    printf("G%d\n%.1f %.1f", ansid - n, ansdis, ansavar);
  }
  return 0;
}
