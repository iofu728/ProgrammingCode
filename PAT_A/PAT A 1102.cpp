/*
 * @Author: gunjianpan
 * @Date:   2018-09-20 12:32:38
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2018-09-20 12:53:10
 */
#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <queue>

using namespace std;

const int MAXN = 11;

struct node {
  int id, left, right;
} A[MAXN];

int n, num = 0;

bool vis[MAXN] = {false};

void layerorder(int root) {
  queue<node> q;
  q.push(A[root]);
  fill(vis, vis + MAXN, false);
  vis[root] = true;
  while (!q.empty()) {
    node top = q.front();
    q.pop();
    if (top.id != root) cout << ' ';
    cout << top.id;
    if (top.left != -1 && !vis[top.left]) {
      q.push(A[top.left]);
      vis[top.left] = true;
    }
    if (top.right != -1 && !vis[top.right]) {
      q.push(A[top.right]);
      vis[top.right] = true;
    }
  }
  cout << endl;
}

void dfs(int root) {
  if (A[root].left != -1) dfs(A[root].left);
  if (num++) cout << ' ';
  cout << root;
  if (A[root].right != -1) dfs(A[root].right);
}

int main(int argc, char const *argv[]) {
  cin >> n;
  for (int i = 0; i < n; ++i) {
    string templeft, tempright;
    cin >> templeft >> tempright;
    A[i].right = templeft != "-" ? atoi(templeft.c_str()) : -1;
    A[i].left = tempright != "-" ? atoi(tempright.c_str()) : -1;
    A[i].id = i;
    if (A[i].left != -1) vis[A[i].left] = true;
    if (A[i].right != -1) vis[A[i].right] = true;
  }
  int root;
  for (int i = 0; i < n; ++i)
    if (!vis[i]) {
      root = i;
      break;
    }
  layerorder(root);
  dfs(root);
  cout << endl;

  return 0;
}
