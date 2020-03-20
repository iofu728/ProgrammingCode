#include <cstdio>
#include <queue>
#include <vector>
using namespace std;

const int maxn = 100;
vector<int> sum;
struct node {
  vector<int> child;
  int layer;

} NODE[maxn];

void BFS(int root) {
  queue<int> Q;
  Q.push(root);
  NODE[root].layer = 0;
  while (!Q.empty()) {
    int front = Q.front();
    if (NODE[front].child.size()) sum[NODE[front].layer]++;
    Q.pop();
    for (int i = 0; i < NODE[front].child.size(); i++) {
      int child = NODE[front].child[i];
      NODE[child].layer = NODE[front].layer + 1;
      Q.push(child);
    }
  }
}
int main() {
  int n, m, st, ed, k;
  scanf("%d%d", &n, &m);

  for (int i = 0; i < m; i++) {
    scanf("%d%d", &st, &k);
    for (int j = 0; j < k; j++) {
      scanf("%d", &NODE[st].child[j]);
    }
  }
  BFS(01);
  int i;
  for (i = 0; i < sum.size() - 2; i++) {
    printf("%d ", sum[i]);
  }
  printf("%d", sum[i]);
}
