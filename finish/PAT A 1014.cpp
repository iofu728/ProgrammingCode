#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;
struct node {
  int poptime = 0, endtime = 0, windows;
  queue<int> q; // 存入花费时间
};
bool cmp(node a, node b) { return a.poptime < b.poptime; }
int main() {
  int n, m, k, q, now = 1;
  cin >> n >> m >> k >> q;
  getchar();
  vector<int> spend(k + 1), end(k + 1);
  bool vis[k + 1] = {true}; // 能否服务判断
  fill(vis, vis + k + 1, true);
  //		for(int i=1;i<=k;++i){
  //		cout<<vis[i]<<" ";
  //	}
  //	cout<<endl;
  for (int i = 1; i < k + 1; ++i) {
    cin >> spend[i];
  }
  getchar();
  vector<node> window(n);
  // 遍历排队区
  for (int i = 1; i <= m; ++i) {
    for (int j = 1; j <= n; ++j) {
      if (now <= k) {
        window[j - 1].q.push(spend[now]);
        if (window[j - 1].endtime >= 540) {
          vis[now] = false; // 前面一位结束时候超时
        }
        window[j - 1].endtime += spend[now];
        if (i == 1) {
          window[j - 1].poptime = window[j - 1].endtime;
        }
        end[now] = window[j - 1].endtime;
        window[j - 1].windows = j - 1;
        ++now;
      }
    }
  }
  //	for(int i=0;i<n;++i){
  //		cout<<window[i].poptime<<" "<<window[i].endtime<<" ";
  //		for(int j=0;j<m;++j){
  //			int temp=window[i].q.front();
  //			cout<<temp<<" ";
  //			window[i].q.pop();
  //		}
  //		cout<<endl;
  //	}
  //	for(int i=1;i<=k;++i){
  //		cout<<vis[i]<<" ";
  //	}
  //	cout<<endl;
  // 遍历等待区
  while (now <= k) {
    sort(window.begin(), window.end(), cmp);
    window[0].q.pop();
    int temptime = window[0].q.front();
    window[0].poptime += temptime;
    if (window[0].endtime >= 540)
      vis[now] = false;
    window[0].endtime += spend[now];
    window[0].q.push(now);
    end[now] = window[0].endtime;
    ++now;
  }
  //	for(int i=1;i<=k;++i){
  //		cout<<vis[i]<<" ";
  //	}
  for (int i = 0; i < q; ++i) {
    int temp;
    scanf("%d", &temp);
    if (vis[temp] == false)
      cout << "Sorry\n";
    else {
      printf("%02d:%02d\n", (end[temp] / 60 + 8), (end[temp] % 60));
    }
  }
  return 0;
}
