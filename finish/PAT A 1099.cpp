#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

const int MAXN = 110;

struct node {
  int id, left, right, layer, data;
} a[110];

int n, b[MAXN], now = 0;

void dfs(int root, int index, int layer) {
  if (a[root].left == -1 && a[root].right == -1) {
    a[root] = {index, a[root].left, a[root].right, layer, b[now++]};
  } else {
    if (a[root].left != -1) dfs(a[root].left, index * 2 + 1, layer + 1);
    a[root] = {index, a[root].left, a[root].right, layer, b[now++]};
    if (a[root].right != -1) dfs(a[root].right, index * 2 + 2, layer + 1);
  }
}

bool layerorder(node a, node b) {
  return a.layer == b.layer ? a.id < b.id : a.layer < b.layer;
}

int main(int argc, char const *argv[]) {
  cin >> n;
  for (int i = 0; i < n; ++i) cin >> a[i].left >> a[i].right;
  for (int i = 0; i < n; ++i) cin >> b[i];
  sort(b, b + n);
  dfs(0, 0, 0);
  sort(a, a + n, layerorder);
  for (int i = 0; i < n; ++i) {
    if (i) cout << ' ';
    cout << a[i].data;
  }
  return 0;
}
