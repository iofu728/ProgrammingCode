#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

const int maxn = 10010;
int n, m;
int value[maxn];
vector<int> G[maxn];
vector<long long> v;
bool vis[maxn];
long long sum = 0, temp = 0;
void DFS(int start) {
  char s[30];
  int length = sprintf(s, "%d", value[start]);
  temp = temp * pow(10, length) + value[start];
  vis[start] = true;
  bool flag = false;
  vector<int> tempv = G[start];
  for (int i = 0; i < tempv.size(); ++i) {
    if (!vis[tempv[i]]) {
      flag = true;
      DFS(tempv[i]);
    }
  }
  if (!flag) {
    sum += temp;
  }
  temp = (temp - value[start]) / pow(10, length);
}

int main() {
  fill(vis, vis + maxn, false);
  cin >> n >> m;
  getchar();
  for (int i = 0; i < n; ++i) {
    cin >> value[i];
  }
  getchar();
  for (int i = 0; i < m; ++i) {
    int x, y;
    scanf("%d %d", &x, &y);
    G[x].push_back(y);
    G[y].push_back(x);
  }

  for (int i = 0; i < n; ++i) {
    if (!vis[i]) {
      sum = 0, temp = 0;
      DFS(i);
      v.push_back(sum);
    }
  }
  if (!v.size()) {
    cout << 0 << endl;
  } else {
    cout << v.size() << endl;
    for (int i = 0; i < v.size() - 1; ++i) {
      cout << v[i] << ' ';
    }
    cout << v[v.size() - 1] << endl;
  }
  return 0;
}
