#include <algorithm>
#include <iostream>
#include <stack>
#include <vector>

using namespace std;
string s1, s2;
long long other = 0;

void dfs(int index1, int index2, int num) {
  // cout << num << ' ' << index1 << ' ' << index2 << ' ' << other << endl;
  if (num < 0) return;
  if (index1 == s1.size() && index2 == s2.size()) {
    if (!num) ++other;
    return;
  }
  if (index1 < s1.size() && s1[index1] == '(') dfs(index1 + 1, index2, num + 1);
  if (index1 < s1.size() && s1[index1] == ')') dfs(index1 + 1, index2, num - 1);
  if (index2 < s2.size() && s2[index2] == '(') dfs(index1, index2 + 1, num + 1);
  if (index2 < s2.size() && s2[index2] == ')') dfs(index1, index2 + 1, num - 1);
}

int main() {
  cin >> s1 >> s2;
  dfs(0, 0, 0);
  cout << other % (10 ^ 9 + 7) << endl;
}
