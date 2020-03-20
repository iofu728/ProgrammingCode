#include <cstdio>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;
const int MAXN = 1009;
int m;

struct node {
  int id, layer;
};

vector<vector<int> > v;

int bfs(node start) {
  bool vis[MAXN] = {false};
  vis[start.id] = true;
  queue<node> q;
  q.push(start);
  int connectNum = 0;
  while (!q.empty()) {
    node top = q.front();
    q.pop();
    int topId = top.id;
    for (int i = 0; i < v[topId].size(); ++i) {
      node next = {v[topId][i], top.layer + 1};
      if (!vis[next.id] && next.layer <= m) {
        q.push(next);
        vis[next.id] = true;
        ++connectNum;
      }
    }
  }
  return connectNum;
}

int main(int argc, char const *argv[]) {
  int n, num, temp;
  cin >> n >> m;
  v.resize(n + 1);
  for (int i = 1; i < n + 1; ++i) {
    cin >> num;
    for (int j = 0; j < num; ++j) {
      cin >> temp;
      v[temp].push_back(i);
    }
  }
  cin >> num;
  for (int i = 0; i < num; ++i) {
    cin >> temp;
    node start = {temp, 0};
    cout << bfs(start) << endl;
  }
  return 0;
}
