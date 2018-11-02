/*
 * @Author: gunjianpan
 * @Date:   2018-10-31 23:37:28
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2018-11-03 00:07:53
 */
#include <iostream>
#include <queue>

using namespace std;

const int MAXN = 22;

struct node {
  int left = -1, right = -1;
} pre[MAXN];

bool havefather[MAXN] = {false}, vis[MAXN] = {false};
int num;

int main(int argc, char const *argv[]) {
  cin >> num;
  for (int i = 0; i < num; ++i) {
    string templ, tempr;
    cin >> templ >> tempr;
    if (templ != "-") pre[i].left = stoi(templ);
    if (templ != "-") havefather[stoi(templ)] = true;
    if (tempr != "-") pre[i].right = stoi(tempr);
    if (tempr != "-") havefather[stoi(tempr)] = true;
  }
  int root = 0, index = 0, laster = -1, breaknum = -1;
  while (havefather[root]) ++root;
  queue<node> q;
  q.push(pre[root]);
  vis[root] = true;
  while (!q.empty()) {
    node top = q.front();
    q.pop();
    ++index;
    if (top.left != -1) {
      if (breaknum != -1) break;
      if (!vis[top.left]) {
        vis[top.left] = true;
        q.push(pre[top.left]);
        laster = top.left;
      }
    } else if (index < num / 2)
      break;
    else
      breaknum = index;
    if (top.right != -1) {
      if (breaknum != -1) break;
      if (!vis[top.right]) {
        vis[top.right] = true;
        q.push(pre[top.right]);
        laster = top.right;
      }
    } else if (index < num / 2)
      break;
    else
      breaknum = index;
  }
  if (index < num)
    cout << "NO " << root << endl;
  else
    cout << "YES " << laster << endl;
  return 0;
}
