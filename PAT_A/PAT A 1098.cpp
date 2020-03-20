/*
 * @Author: gunjianpan
 * @Date:   2018-09-17 14:10:33
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2018-09-17 14:28:14
 */

#include <algorithm>
#include <iostream>

using namespace std;

void downadjust(int left, int right) {
  int i = left, j = 2 * i;
  while (j <= right) {
  }
}

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
    cout << "Heap Sort" << endl;
    diff = n - 1;
    while (diff > 0 && change[diff] >= change[diff - 1]) --diff;
    swap(change[0], change[diff]);
    int i = 0, j = i * 2 + 1;
    while (j <= diff - 1) {
      if (j + 1 < diff - 1 && change[j] < change[j + 1]) j = j + 1;
      if (change[i] < change[j]) {
        swap(change[i], change[j]);
        i = j;
        j = i * 2 + 1;
      } else {
        break;
      }
    }
  } else {
    cout << "Insertion Sort" << endl;
    sort(change, change + diff + 2);
  }
  for (int i = 0; i < n; ++i) {
    if (i) cout << ' ';
    cout << change[i];
  }
  return 0;
}
