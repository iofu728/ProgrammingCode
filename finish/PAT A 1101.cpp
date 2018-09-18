/*
 * @Author: gunjianpan
 * @Date:   2018-09-18 14:38:34
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2018-09-18 14:47:43
 */
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

const int MAXN = 100010;
int pre[MAXN], patation[MAXN];
std::vector<int> v;

int main(int argc, char const *argv[]) {
  int n, temp, big = 0;
  cin >> n;
  for (int i = 0; i < n; ++i) {
    cin >> pre[i];
    patation[i] = pre[i];
  }
  sort(patation, patation + n);
  for (int i = 0; i < n; ++i) {
    if (pre[i] == patation[i] && pre[i] > big) v.push_back(pre[i]);
    if (pre[i] > big) {
      big = pre[i];
    }
  }

  cout << v.size() << endl;
  for (int i = 0; i < v.size(); ++i) {
    if (i) cout << ' ';
    cout << v[i];
  }
  cout << endl;
  return 0;
}
