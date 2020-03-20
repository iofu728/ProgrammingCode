#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int colorlike[201], temp[10001], dp[10001];
int main(int argc, char const *argv[]) {
  int n, m, l, a, num = 0, maxn = 0;
  fill(colorlike, colorlike + 201, 0);
  cin >> n;
  getchar();
  cin >> m;
  for (int i = 1; i <= m; ++i) {
    cin >> a;
    colorlike[a] = i;
  }
  getchar();
  cin >> l;
  for (int i = 0; i < l; ++i) {
    cin >> a;
    if (colorlike[a]) {
      temp[num++] = colorlike[a];
    }
  }
  for (int i = 0; i < num; ++i) {
    dp[i] = 1;
    for (int j = 0; j < i; ++j) {
      if (temp[i] >= temp[j]) {
        dp[i] = max(dp[i], dp[j] + 1);
      }
    }
    maxn = max(dp[i], maxn);
  }
  cout << maxn;
  return 0;
}