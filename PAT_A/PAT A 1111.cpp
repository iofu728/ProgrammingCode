/*
 * @Author: gunjianpan
 * @Date:   2019-03-07 13:17:16
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2019-03-08 12:52:01
 */
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

const int MAXN_NODE = 510;
const int INF = 0x3fffffff;

int path[MAXN_NODE][MAXN_NODE];
int cost[MAXN_NODE][MAXN_NODE];

bool haveSpace[MAXN_NODE] = {false};
int num, d[MAXN_NODE], nodeNum = INF;
std::vector<int> pre[MAXN_NODE], bestTime, bestDis;

void Dijkstra(int s, int type) {
  fill(d, d + MAXN_NODE, INF);
  d[s] = 0;
  for (int i = 0; i < num; ++i) {
    int u = -1, MIN = INF;
    for (int j = 0; j < num; ++j) {
      if (!haveSpace[j] && d[j] < MIN) {
        MIN = d[j];
        u = j;
      }
    }
    if (u == -1) return;
    haveSpace[u] = true;
    for (int j = 0; j < num; ++j) {
      if (!haveSpace[j]) {
        int value = type == 1 ? path[u][j] : cost[u][j];
        if (d[u] + value < d[j]) {
          d[j] = d[u] + value;
          pre[j].clear();
          pre[j].push_back(u);
        } else if (d[u] + value == d[j]) {
          pre[j].push_back(u);
        }
      }
    }
  }
}

void dfsTime(int now, vector<int> temp) {
  temp.push_back(now);
  if (temp.size() > nodeNum) return;
  if (!pre[now].size()) {
    if (temp.size() < nodeNum) {
      nodeNum = temp.size();
      bestTime = temp;
    }
    return;
  }
  for (int i = 0; i < pre[now].size(); ++i) dfsTime(pre[now][i], temp);
}

void dfsDis(int now, vector<int> temp, int spendTime) {
  temp.push_back(now);
  if (spendTime > nodeNum) return;
  if (!pre[now].size()) {
    if (spendTime < nodeNum) {
      nodeNum = spendTime;
      bestDis = temp;
    }
    return;
  }
  for (int i = 0; i < pre[now].size(); ++i)
    dfsDis(pre[now][i], temp, spendTime + cost[pre[now][i]][now]);
}

void printResult(int type) {
  std::vector<int> v = type == 1 ? bestDis : bestTime;
  for (int i = v.size() - 1; i >= 0; --i) {
    if (i != v.size() - 1) cout << " ->";
    cout << ' ' << v[i];
  }
}

int main(int argc, char const *argv[]) {
  fill(path[0], path[0] + MAXN_NODE * MAXN_NODE, INF);
  fill(cost[0], cost[0] + MAXN_NODE * MAXN_NODE, INF);
  fill(haveSpace, haveSpace + MAXN_NODE, false);
  int collase, begin, end;
  cin >> num >> collase;

  for (int i = 0; i < collase; ++i) {
    int tempBegin, tempEnd, oneWay, distance, tempTime;
    cin >> tempBegin >> tempEnd >> oneWay >> distance >> tempTime;
    path[tempBegin][tempEnd] = distance;
    cost[tempBegin][tempEnd] = tempTime;
    if (!oneWay) {
      path[tempEnd][tempBegin] = distance;
      cost[tempEnd][tempBegin] = tempTime;
    }
  }
  cin >> begin >> end;

  vector<int> test;
  Dijkstra(begin, 1);
  dfsDis(end, test, 0);
  int dis = d[end];

  fill(haveSpace, haveSpace + MAXN_NODE, false);
  nodeNum = INF;

  Dijkstra(begin, 0);
  dfsTime(end, test);
  int times = d[end];
  bool same = bestDis.size() == bestTime.size();
  if (same) {
    for (int i = 0; i < bestTime.size(); ++i)
      if (bestDis[i] != bestTime[i]) {
        same = false;
        break;
      }
  }
  if (same) {
    cout << "Distance = " << dis << "; Time = " << times << ":";
    printResult(1);
  } else {
    cout << "Distance = " << dis << ":";
    printResult(1);
    cout << endl << "Time = " << times << ":";
    printResult(0);
    cout << endl;
  }

  return 0;
}
