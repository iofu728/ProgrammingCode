/*
 * @Author: gunjianpan
 * @Date:   2018-09-20 23:37:05
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2018-09-23 20:58:33
 */
#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

const int MAXN = 410;
int pre[MAXN], n, k, p, maxindex = 1, maxfacSum = -1;
vector<int> path;

void dfs(vector<int> &nowpath, int tempsum, int tempindex, int facsum) {
  if (nowpath.size() >= k || tempsum >= n || !tempindex) {
    if (nowpath.size() == k && tempsum == n && facsum > maxfacSum) {
      path = nowpath;
      maxfacSum = facsum;
    }
    return;
  }
  while (tempindex) {
    if (tempsum + pre[tempindex] <= n) {
      nowpath.push_back(tempindex);
      dfs(nowpath, tempsum + pre[tempindex], tempindex, facsum + tempindex);
      nowpath.pop_back();
    }
    if (tempindex == 1) return;
    --tempindex;
  }
}

int main(int argc, char const *argv[]) {
  cin >> n >> k >> p;
  pre[0] = 0;
  for (; pre[maxindex - 1] < n && maxindex < n; ++maxindex)
    pre[maxindex] = pow(maxindex, p);
  std::vector<int> v;
  dfs(v, 0, maxindex - 1, 0);
  if (!path.size()) {
    cout << "Impossible";
  } else {
    cout << n << " =";
    for (int i = 0; i < path.size(); ++i) {
      if (i) cout << " +";
      cout << ' ' << path[i] << '^' << p;
    }
  }

  return 0;
}
