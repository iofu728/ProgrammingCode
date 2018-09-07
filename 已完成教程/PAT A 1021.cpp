#include <algorithm>
#include <iostream>
#include <set>
#include <vector>
using namespace std;

const int maxn = 10010;
vector<int> G[maxn];
vector<int> temp;
set<int> s;
int n, maxheight = 0;
bool vis[maxn] = {false};

void DFS(int now, int height) {
  if (height >= maxheight) {
    if (height > maxheight) {
      temp.clear();
    }
    temp.push_back(now);
    maxheight = height;
    //		for(int i=0;i<temp.size();++i){
    //			cout<<temp[i]<<" ";
    //		}
    //		cout<<endl;
  }
  vis[now] = true;
  for (int i = 0; i < G[now].size(); ++i) {
    if (vis[G[now][i]] == false) {
      DFS(G[now][i], height + 1);  //Íò¶ñÖ®Ô´++height
    }
  }
}
int main() {
  scanf("%d\n", &n);
  int size = 0, start = 0;
  for (int i = 0; i < n - 1; ++i) {
    int x, y;
    scanf("%d %d", &x, &y);
    G[x].push_back(y);
    G[y].push_back(x);
  }
  fill(vis, vis + maxn, false);
  for (int i = 1; i <= n; ++i) {
    if (vis[i] == false) {
      DFS(i, 1);
      if (i == 1) {
        for (int j = 0; j < temp.size(); ++j) {
          s.insert(temp[j]);
          if (j == 0) start = temp[j];
        }
      }
      ++size;
    }
  }
  //	cout<<size;
  if (size > 1) {
    printf("Error: %d components", size);
  } else {
    temp.clear();
    fill(vis, vis + maxn, false);
    maxheight = 0;
    DFS(start, 1);
    for (int i = 0; i < temp.size(); ++i) {
      s.insert(temp[i]);
    }
    for (auto it = s.begin(); it != s.end(); ++it) {
      printf("%d\n", *it);
    }
  }
  return 0;
}
