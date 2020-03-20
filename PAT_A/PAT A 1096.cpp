/*
 * @Author: gunjianpan
 * @Date:   2018-09-17 13:05:39
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2018-09-17 13:20:11
 */
#include <cmath>
#include <iostream>

using namespace std;

int main(int argc, char const *argv[]) {
  long long n, temp;
  cin >> n;
  int maxn = sqrt(n), left = 0, len = 0;
  for (int i = 2; i <= maxn; ++i) {
    int j, temp = 1;
    for (j = i; j <= maxn; ++j) {
      temp *= j;
      if (n % temp) break;
    }
    if (j - i > len) {
      len = j - i;
      left = i;
    }
  }
  if (!left) {
    cout << 1 << endl << n;
  } else {
    cout << len << endl;
    for (int i = 0; i < len; ++i) {
      if (i) cout << '*';
      cout << (left + i);
    }
  }

  return 0;
}
