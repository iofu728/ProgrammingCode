#include <algorithm>
#include <cstring>
#include <iostream>
#include <vector>
using namespace std;
char name[40001][5];
bool cmp(int a, int b) { return strcmp(name[a], name[b]) < 0; }
int main() {
  int n, m, num, cid;
  scanf("%d %d", &n, &m);
  vector<int> course[m + 1];
  for (int i = 0; i < n; ++i) {
    scanf("%s %d", name[i], &num);
    for (int j = 0; j < num; ++j) {
      scanf("%d", &cid);
      course[cid].push_back(i);
    }
  }
  for (int i = 1; i <= m; ++i) {
    vector<int> temp = course[i];
    sort(temp.begin(), temp.end(), cmp);
    cout << i << " " << temp.size() << endl;
    for (int j = 0; j < temp.size(); ++j) {
      printf("%s\n", name[temp[j]]);
    }
  }
  return 0;
}
