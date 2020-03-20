/*
 * @Author: gunjianpan
 * @Date:   2018-09-29 19:58:35
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2018-09-29 21:15:34
 */
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;
const int MAXN = 1010;
std::vector<int> pre[MAXN], merges;
std::vector<vector<int> > v, course;
bool vis[MAXN] = {false};

bool sortnum(vector<int> a, vector<int> b) {
  return a.size() == b.size() || a.size() > b.size();
}

int main(int argc, char const *argv[]) {
  int n, num, temp, count = 0;
  cin >> n;
  for (int i = 0; i < n; ++i) {
    scanf("%d:", &num);
    merges.clear();
    fill(vis, vis + MAXN, false);
    count = 0;
    for (int j = 0; j < num; ++j) {
      cin >> temp;
      pre[i].push_back(temp);
      for (int k = 0; k < v.size(); ++k)
        if (!vis[k] && std::find(course[k].begin(), course[k].end(), temp) !=
                           course[k].end()) {
          merges.push_back(k);
          vis[k] = true;
        }
    }
    if (!merges.size()) {
      std::vector<int> top;
      top.push_back(i);
      v.push_back(top);
      course.push_back(pre[i]);
    } else {
      sort(merges.begin(), merges.end());
      int top = merges[0];
      v[top].push_back(i);
      course[top].insert(course[top].end(), pre[i].begin(), pre[i].end());
      for (int j = 1; j < merges.size(); ++j) {
        v[top].insert(v[top].end(), v[merges[j] - count].begin(),
                      v[merges[j] - count].end());
        course[top].insert(course[top].end(), course[merges[j] - count].begin(),
                           course[merges[j] - count].end());
        v.erase(v.begin() + merges[j] - count);
        course.erase(course.begin() + merges[j] - count);
        ++count;
      }
    }
  }
  cout << v.size() << endl;
  sort(v.begin(), v.end(), sortnum);
  for (int i = 0; i < v.size(); ++i) {
    if (i) cout << ' ';
    cout << v[i].size();
  }
  return 0;
}
