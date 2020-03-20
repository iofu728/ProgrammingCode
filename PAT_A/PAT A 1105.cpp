/*
 * @Author: gunjianpan
 * @Date:   2018-09-28 19:42:10
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2018-09-28 20:22:38
 */
#include <algorithm>
#include <cmath>
#include <iostream>

using namespace std;

bool bigsort(int a, int b) { return a > b; }

int main(int argc, char const *argv[]) {
  int num, n, m, t = 0;
  cin >> num;
  n = sqrt(num);
  while (num % n && n > 0) --n;
  m = num / n;
  int matric[m][n], pre[num];
  for (int i = 0; i < num; ++i) cin >> pre[i];
  sort(pre, pre + num, bigsort);
  for (int i = 0; i < m; ++i) {
    for (int j = i; j < n - i && t < num; ++j) matric[i][j] = pre[t++];
    for (int j = i + 1; j < m - i && t < num; ++j)
      matric[j][n - i - 1] = pre[t++];
    for (int j = n - 2 - i; j >= i && t < num; --j)
      matric[m - i - 1][j] = pre[t++];
    for (int j = m - i - 2; j > i && t < num; --j) matric[j][i] = pre[t++];
  }
  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j) {
      if (j) cout << ' ';
      cout << matric[i][j];
    }
    cout << endl;
  }

  return 0;
}
