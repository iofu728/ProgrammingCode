/*
 * @Author: gunjianpan
 * @Date:   2018-09-13 19:57:58
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2018-09-13 20:15:13
 */
#include <algorithm>
#include <iostream>

using namespace std;

int main(int argc, char const *argv[]) {
  long long n, m;
  cin >> n >> m;
  long long wait[n];
  for (int i = 0; i < n; ++i) cin >> wait[i];
  sort(wait, wait + n);
  int left = 0, right = n - 1, maxlength = 0;
  for (int i = 0; i < n; ++i) {
    left = i;
    while (wait[right] <= wait[i] * m && right < n - 1) ++right;
    while (wait[right] > wait[i] * m && right > i) --right;
    if (right - left + 1 > maxlength) maxlength = right - left + 1;
  }
  cout << maxlength;
  return 0;
}
