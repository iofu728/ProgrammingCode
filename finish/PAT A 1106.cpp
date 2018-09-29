/*
 * @Author: gunjianpan
 * @Date:   2018-09-29 19:20:23
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2018-09-29 19:44:29
 */
#include <cmath>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

const int MAXN = 100010;

struct node {
  int id, layer;
};

std::vector<int> v[MAXN];
int n, num, temp, minlayer = 0xfffffff, minnum = 0;
double price, pre;
bool vis[MAXN] = {false};

int main(int argc, char const *argv[]) {
  cin >> n >> pre >> price;
  for (int i = 0; i < n; ++i) {
    cin >> num;
    for (int j = 0; j < num; ++j) {
      cin >> temp;
      v[i].push_back(temp);
    }
  }
  queue<node> q;
  node start = {0, 0};
  vis[0] = true;
  q.push(start);
  while (!q.empty()) {
    node top = q.front();
    q.pop();
    vis[top.id] = true;
    if (top.layer > minlayer) break;
    if (!v[top.id].size()) {
      if (top.layer < minlayer) {
        minlayer = top.layer;
        minnum = 1;
      } else if (top.layer == minlayer)
        ++minnum;
      continue;
    }
    for (int i = 0; i < v[top.id].size(); ++i) {
      if (!vis[v[top.id][i]]) {
        node next = {v[top.id][i], top.layer + 1};
        q.push(next);
      }
    }
  }
  printf("%.4lf %d", pre * pow(1 + price / 100, minlayer), minnum);

  return 0;
}
