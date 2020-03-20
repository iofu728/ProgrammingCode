/*
 * @Author: gunjianpan
 * @Date:   2018-09-15 14:30:48
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2018-09-15 15:25:32
 */
#include <algorithm>
#include <iostream>

using namespace std;

int main(int argc, char const *argv[]) {
  int n, diff = 0;
  bool isinsert = true;
  cin >> n;
  int pre[n], change[n];
  for (int i = 0; i < n; ++i) cin >> pre[i];
  for (int i = 0; i < n; ++i) cin >> change[i];
  while (change[diff] < change[diff + 1] && diff < n - 1) ++diff;
  for (int i = diff + 1; i < n; ++i)
    if (pre[i] != change[i]) isinsert = false;
  if (!isinsert) {
    cout << "Merge Sort" << endl;
    int k = 1, flag = 1;
    while (flag) {
      flag = 0;
      for (int i = 0; i < n; ++i)
        if (pre[i] != change[i]) flag = 1;
      k = k * 2;
      for (int i = 0; i < n / k; ++i) sort(pre + i * k, pre + (i + 1) * k);
      sort(pre + n / k * k, pre + n);
    }
  } else {
    cout << "Insertion Sort" << endl;
    sort(pre, pre + diff + 2);
  }
  for (int i = 0; i < n; ++i) {
    if (i) cout << ' ';
    cout << pre[i];
  }
  return 0;
}
