/*
 * @Author: gunjianpan
 * @Date:   2018-09-11 20:11:49
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2018-09-11 22:34:53
 */
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

struct node {
  int ge, gi, rank, id;
  vector<int> application;
};

bool comparenode(node a, node b) {
  return a.ge + a.gi == b.ge + b.gi ? (a.ge == b.ge ? a.id < b.id : a.ge > b.ge)
                                    : a.ge + a.gi > b.ge + b.gi;
}

bool compareplace(node a, node b) { return a.id < b.id; }
int main(int argc, char const *argv[]) {
  int n, m, k, want;
  cin >> n >> m >> k;
  vector<int> places(m);
  vector<node> v;
  vector<vector<node> > result(m);
  for (int i = 0; i < m; ++i) cin >> places[i];
  for (int i = 0; i < n; ++i) {
    node temp;
    temp.id = i;
    cin >> temp.ge >> temp.gi;
    for (int i = 0; i < k; ++i) {
      cin >> want;
      temp.application.push_back(want);
    }
    v.push_back(temp);
  }
  sort(v.begin(), v.end(), comparenode);
  for (int i = 0; i < n; ++i) {
    if (i) {
      if (v[i].ge == v[i - 1].ge && v[i].gi == v[i - 1].gi) {
        v[i].rank = v[i - 1].rank;
        for (int j = 0; j < v[i].application.size(); ++j) {
          want = v[i].application[j];
          if (places[want] > result[want].size() ||
              (places[want] <= result[want].size() &&
               result[want][places[want] - 1].rank == v[i].rank)) {
            result[want].push_back(v[i]);
            break;
          }
        }
      } else {
        v[i].rank = i;
        for (int j = 0; j < v[i].application.size(); ++j) {
          want = v[i].application[j];
          if (places[want] > result[want].size()) {
            result[want].push_back(v[i]);
            break;
          }
        }
      }
    } else {
      v[i].rank = 0;
      result[v[i].application[0]].push_back(v[i]);
    }
  }
  for (int i = 0; i < m; ++i) {
    sort(result[i].begin(), result[i].end(), compareplace);
    for (int j = 0; j < result[i].size(); ++j) {
      if (j) cout << ' ';
      cout << result[i][j].id;
    }
    cout << endl;
  }

  return 0;
}
