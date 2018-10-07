/*
 * @Author: gunjianpan
 * @Date:   2018-10-07 15:14:51
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2018-10-07 15:42:26
 */
#include <algorithm>
#include <deque>
#include <iostream>
#include <vector>

using namespace std;

struct node {
  int height;
  string name;
};

std::vector<node> v;
std::deque<int> dq, dqo;

bool compareheight(node a, node b) {
  return a.height == b.height ? a.name < b.name : a.height > b.height;
}

void structdq(int n) {
  for (int i = 0; i < n; ++i)
    if (i >> 1 << 1 == i)
      dq.push_back(i);
    else
      dq.push_front(i);
  dqo.assign(dq.begin(), dq.end());
  if (n >> 1 << 1 == n)
    dqo.pop_front();
  else
    dqo.pop_back();
}

int main(int argc, char const *argv[]) {
  int n, m;
  cin >> n >> m;
  v.resize(n);

  for (int i = 0; i < n; ++i) cin >> v[i].name >> v[i].height;
  sort(v.begin(), v.end(), compareheight);

  structdq(n / m + (!n % m ? 0 : 1));
  for (int i = 0; i < n % m; ++i) {
    for (int j = 0; j < n / m + 1; ++j) {
      if (j) cout << ' ';
      cout << v[dq[j] + i * (n / m + 1)].name;
    }
    cout << endl;
  }

  for (int i = n % m; i < m; ++i) {
    for (int j = 0; j < n / m; ++j) {
      if (j) cout << ' ';
      cout << v[dqo[j] + (n % m) * (n / m + 1) + (i - n % m) * (n / m)].name;
    }
    cout << endl;
  }

  return 0;
}
