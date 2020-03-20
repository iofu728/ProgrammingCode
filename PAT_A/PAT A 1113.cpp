/*
 * @Author: gunjianpan
 * @Date:   2019-03-11 11:08:04
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2019-03-12 23:11:55
 */
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
  int n, sum = 0, halfsum = 0;

  cin > n;
  vector<int> v(n);

  for (int i = 0; i < n; ++i) {
    cin >> v[i];
    sum += v[i];
  }

  sort(v.begin(), v.end());

  for (int i = 0; i < n / 2; ++i) halfsum += v[i];

  cout << n % 2 << ' ' << sum - 2 * halfsum;
  return 0;
}
