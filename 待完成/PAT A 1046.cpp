#include <algorithm>
#include <cstdio>
#include <iostream>
using namespace std;

int main() {
  int n, m, a, b, c, d, e, f;
  int sum = 0;
  int dis[100005];
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d", &dis[i]);
    sum += dis[i];
    dis[i] = sum;
  }

  scanf("%d", &m);
  for (int i = 0; i < m; i++) {
    scanf("%d", &a);
    scanf("%d", &b);
    d = 0;
    if (a > b) swap(a, b);
    if (a == 1)
      d = dis[b - 2];
    else {
      d = dis[b - 2] - dis[a - 2];
    }

    if (d < sum / 2)
      printf("%d\n", d);
    else
      printf("%d\n", sum - d);
  }
  cin >> f;
  cout << dis[f] << endl;
}
