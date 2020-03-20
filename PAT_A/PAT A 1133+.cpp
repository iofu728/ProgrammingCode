#include <cstdio>
#include <vector>
using namespace std;

const int maxn = 100001;
struct node {
  int data;
  int nextid;
} G[maxn];
vector<int> prez, inz, postz;

int main() {
  int n, m, k;
  scanf("%d%d%d", &n, &m, &k);
  int idx;
  for (int i = 0; i < m; i++) {
    scanf("%d", &idx);
    scanf("%d %d", &G[idx].data, &G[idx].nextid);
  }
  int nowid = n;
  for (int i = 0; i < m; i++) {
    if (G[nowid].data < 0)
      prez.push_back(nowid);
    else if (G[nowid].data > k)
      postz.push_back(nowid);
    else
      inz.push_back(nowid);
    nowid = G[nowid].nextid;
  }
  for (int i = 0; i < prez.size(); i++) {
    printf("%05d %d ", prez[i], G[prez[i]].data);
    if (i + 1 < prez.size())
      printf("%05d\n", prez[i + 1]);
    else if (inz.size() != 0)
      printf("%05d\n", inz[0]);
    else if (postz.size() != 0)
      printf("%05d\n", postz[0]);
    else
      printf("-1\n");
  }
  for (int i = 0; i < inz.size(); i++) {
    printf("%05d %d ", inz[i], G[inz[i]].data);
    if (i + 1 < inz.size())
      printf("%05d\n", inz[i + 1]);
    else if (postz.size() != 0)
      printf("%05d\n", postz[0]);
    else
      printf("-1\n");
  }
  for (int i = 0; i < postz.size(); i++) {
    printf("%05d %d ", postz[i], G[postz[i]].data);
    if (i + 1 < postz.size())
      printf("%05d\n", postz[i + 1]);
    else
      printf("-1\n");
  }
  return 0;
}
