/*
 * @Author: gunjianpan
 * @Date:   2018-09-11 19:34:19
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2018-09-11 20:00:54
 */
#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

double result = 0.0, p, r;

struct node {
  int volume;
  vector<int> child;
};

vector<node> v;

void dfs(int node, int depth) {
  if (!v[node].child.size()) {
    result += v[node].volume * pow(1 + r, depth);
  }
  for (int i = 0; i < v[node].child.size(); ++i) {
    dfs(v[node].child[i], depth + 1);
  }
}

int main(int argc, char const *argv[]) {
  int n, num, child;
  cin >> n >> p >> r;
  v.resize(n);
  r /= 100;
  for (int i = 0; i < n; ++i) {
    cin >> num;
    if (!num) {
      cin >> v[i].volume;
    } else {
      for (int j = 0; j < num; ++j) {
        cin >> child;
        v[i].child.push_back(child);
      }
    }
  }
  dfs(0, 0);
  printf("%.1f", result * p);
  return 0;
}
