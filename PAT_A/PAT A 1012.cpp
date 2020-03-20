#include <algorithm>
#include <cstdio>
using namespace std;

struct node {
  int num, c, m, e, a;
  int rankc, rankm, ranke, ranka;
} NODE[2010];
bool cmpa(node A, node B) { return A.a > B.a; }
bool cmpc(node A, node B) { return A.c > B.c; }
bool cmpm(node A, node B) { return A.m > B.m; }
bool cmpe(node A, node B) { return A.e > B.e; }
int main() {
  int n, m;
  char ml[4] = {'A', 'C', 'M', 'E'};
  scanf("%d %d", &n, &m);
  int search[m];
  for (int i = 0; i < n; i++) {
    scanf("%d %d %d %d", &NODE[i].num, &NODE[i].c, &NODE[i].m, &NODE[i].e);
    NODE[i].a = (NODE[i].c + NODE[i].e + NODE[i].m) / 3;
  }
  for (int i = 0; i < m; i++) {
    scanf("%d", &search[i]);
  }
  sort(NODE, NODE + n, cmpa);
  for (int i = 0; i < n; i++) {
    NODE[i].ranka = i + 1;
  }
  sort(NODE, NODE + n, cmpc);
  for (int i = 0; i < n; i++) {
    NODE[i].rankc = i + 1;
  }
  sort(NODE, NODE + n, cmpm);
  for (int i = 0; i < n; i++) {
    NODE[i].rankm = i + 1;
  }
  sort(NODE, NODE + n, cmpe);
  for (int i = 0; i < n; i++) {
    NODE[i].ranke = i + 1;
  }

  int current, Lrank, mll;
  for (int i = 0; i < m; i++) {
    Lrank = n + 1;
    current = -1;
    mll = 0;
    for (int j = 0; j < n; j++) {
      if (NODE[j].num == search[i]) {
        current = j;
      }
    }
    if (current == -1) {
      printf("N/A\n");
    } else {
      if (NODE[current].ranka < Lrank) {
        Lrank = NODE[current].ranka;
        mll = 0;
      }
      if (NODE[current].rankc < Lrank) {
        Lrank = NODE[current].rankc;
        mll = 1;
      }
      if (NODE[current].rankm < Lrank) {
        Lrank = NODE[current].rankm;
        mll = 2;
      }
      if (NODE[current].ranke < Lrank) {
        Lrank = NODE[current].ranke;
        mll = 3;
      }
      printf("%d %c\n", Lrank, ml[mll]);
    }
  }
  return 0;
}
