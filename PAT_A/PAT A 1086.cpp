/*
 * @Author: gunjianpan
 * @Date:   2018-09-13 20:39:32
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2018-09-13 21:36:42
 */
#include <iostream>
#include <stack>
#include <vector>

using namespace std;

vector<int> pre, in, post;

void postorder(int root, int start, int end) {
  if (start > end) return;
  int temp = start;
  while (pre[root] != in[temp] && temp < end) ++temp;
  postorder(root + 1, start, temp - 1);
  postorder(root + temp - start + 1, temp + 1, end);
  post.push_back(pre[root]);
}

int main(int argc, char const *argv[]) {
  int n, num;
  string str;
  stack<int> s;
  cin >> n;
  while (cin >> str) {
    if (str == "Push") {
      cin >> num;
      pre.push_back(num);
      s.push(num);
    } else {
      in.push_back(s.top());
      s.pop();
    }
  }
  postorder(0, 0, n - 1);
  for (int i = 0; i < n; ++i) {
    if (i) cout << ' ';
    cout << post[i];
  }
  return 0;
}
