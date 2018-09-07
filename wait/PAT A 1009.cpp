#include <cstdio>
#include <iostream>
#include <map>
#include <vector>
using namespace std;

struct node {
  int ploy;
  double num;
};
vector<node> v, s;
map<int, double, greater<int> > mmp;

int main() {
  int n, m;
  cin >> n;
  node temp;
  for (int i = 0; i < n; ++i) {
    cin >> temp.ploy >> temp.num;
    v.push_back(temp);
  }
  cin >> m;
  for (int i = 0; i < m; ++i) {
    cin >> temp.ploy >> temp.num;
    s.push_back(temp);
    for (int j = 0; j < n; ++j) {
      int t = v[j].ploy + temp.ploy;
      map<int, double>::iterator it = mmp.find(t);
      if (it == mmp.end()) {
        mmp[t] = v[j].num * temp.num;
      } else
        mmp[t] += v[j].num * temp.num;
    }
  }

  for (map<int, double>::iterator it = mmp.begin(); it != mmp.end(); ++it) {
    if (it->second == 0) mmp.erase(it);
  }
  cout << mmp.size();
  for (map<int, double>::iterator it = mmp.begin(); it != mmp.end(); ++it) {
    printf(" %d %.1lf", it->first, it->second);
  }
  printf("\n");
  return 0;
}
