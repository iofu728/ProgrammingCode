/*
 * @Author: gunjianpan
 * @Date:   2018-09-28 19:29:58
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2018-09-28 19:34:31
 */
#include <iostream>

using namespace std;

const int MAXN = 100010;

int main(int argc, char const *argv[]) {
  int n;
  double pre[MAXN], sum = 0.0;

  cin >> n;
  for (int i = 1; i <= n; ++i) {
    cin >> pre[i];
    sum += pre[i] * i * (n + 1 - i);
  }

  printf("%.2lf\n", sum);
  return 0;
}
