/*
 * @Author: gunjianpan
 * @Date:   2018-09-13 21:37:07
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2018-09-13 23:42:32
 */

#include <iostream>
#include <map>
#include <vector>

using namespace std;

const int INF = 0x3fffffff;
const int MAXN = 209;

struct node {
  int next, spend;
};

std::vector<node> v[MAXN];
bool vis[MAXN] = {false};
std::vector<string> city;
std::vector<int> happy, pre[MAXN], path, temppath, totalhappy;
std::map<string, int> string2int;
int n, k, happiness, rom, d[MAXN], optvalue = 0, avg = 0;

void Dijkstra(int start) {
  fill(d, d + MAXN, INF);
  d[start] = 0;
  for (int i = 0; i < n; ++i) {
    int u = -1, MIN = INF;
    for (int j = 0; j < n; ++j) {
      if (!vis[j] && d[j] < MIN) {
        u = j;
        MIN = d[j];
      }
    }
    if (u == -1) return;
    vis[u] = true;
    for (int j = 0; j < v[u].size(); ++j) {
      int temp = v[u][j].next;
      if (!vis[temp]) {
        if (d[u] + v[u][j].spend < d[temp]) {
          d[temp] = d[u] + v[u][j].spend;
          pre[temp].clear();
          pre[temp].push_back(u);
        } else {
          pre[temp].push_back(u);
        }
      }
    }
  }
}

void dfs(int now, int temphappy) {
  temppath.push_back(now);
  if (!now) {
    // cout << optvalue << ' ' << temphappy + happy[now] << endl;
    if (optvalue < temphappy + happy[now] ||
        (optvalue == temphappy + happy[now] && temppath.size() < path.size())) {
      optvalue = temphappy + happy[now];
      avg = optvalue / (temppath.size() - 1);
      path = temppath;
    }
    totalhappy.push_back(temphappy + happy[now]);
    temppath.pop_back();
    return;
  }
  for (int i = 0; i < pre[now].size(); ++i) {
    dfs(pre[now][i], temphappy + happy[pre[now][i]]);
  }
  temppath.pop_back();
}

int main(int argc, char const *argv[]) {
  string str, str2;
  cin >> n >> k >> str;
  city.push_back(str);
  happy.push_back(0);
  string2int[str] = 0;
  for (int i = 1; i < n; ++i) {
    cin >> str >> happiness;
    happy.push_back(happiness);
    city.push_back(str);
    string2int[str] = i;
    if (str == "ROM") rom = i;
  }
  for (int i = 0; i < k; ++i) {
    node temp;
    cin >> str >> str2 >> temp.spend;
    temp.next = string2int[str2];
    v[string2int[str]].push_back(temp);
    temp.next = string2int[str];
    v[string2int[str2]].push_back(temp);
  }
  Dijkstra(0);
  dfs(rom, happy[rom]);
  cout << totalhappy.size() << ' ' << d[rom] << ' ' << optvalue << ' ' << avg
       << endl;
  for (int i = path.size() - 1; i >= 1; --i) cout << city[path[i]] << "->";
  cout << "ROM";
  return 0;
}
