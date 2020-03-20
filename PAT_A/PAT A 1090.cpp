/*
 * @Author: gunjianpan
 * @Date:   2018-09-15 15:39:37
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2018-09-15 16:57:00
 */
#include <cmath>
#include <iostream>
#include <stack>
#include <vector>

using namespace std;

struct node {
  int id, layer;
};

int main(int argc, char const *argv[]) {
  int n, start, maxlayer = 0, father, maxnum = 1;
  double p, r;
  cin >> n >> p >> r;
  vector<int> pre[n];
  bool vis[n];
  fill(vis, vis + n, false);
  stack<node> s;
  for (int i = 0; i < n; ++i) {
    cin >> father;
    if (father == -1) {
      start = i;
      node temp = {i, 1};
      s.push(temp);
      vis[i] = true;
    } else {
      pre[father].push_back(i);
    };
  };
  while (!s.empty()) {
    node front = s.top();
    s.pop();
    for (int i = 0; i < pre[front.id].size(); ++i) {
      int maybe = pre[front.id][i];
      if (!vis[maybe]) {
        node temp = {maybe, front.layer + 1};
        s.push(temp);
        if (temp.layer > maxlayer) {
          maxlayer = temp.layer;
          maxnum = 1;
        } else if (temp.layer == maxlayer) {
          ++maxnum;
        }
      }
    }
  }
  printf("%.2lf %d\n", p * pow(1 + r / 100, maxlayer - 1), maxnum);

  return 0;
}
