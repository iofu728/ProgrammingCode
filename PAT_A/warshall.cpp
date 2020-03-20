/*
 * @Author: gunjianpan
 * @Date:   2018-10-18 16:50:17
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2018-10-18 17:03:40
 */
#include <iostream>

using namespace std;

int main(int argc, char const *argv[]) {
  int n;
  cin >> n;
  int pre[n][n], next[n][n];
  for (int i = 0; i < n; ++i)
    for (int j = 0; j < n; ++j) cin >> pre[i][j];
  for (int k = 0; k < n; ++k) {
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < n; ++j)
        next[i][j] = pre[i][j] || (pre[i][k] && pre[k][j]);
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        if (j) cout << ' ';
        cout << next[i][j];
        pre[i][j] = next[i][j];
      }
      cout << endl;
    }
    cout << endl;
  }
  return 0;
}
