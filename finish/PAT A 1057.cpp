#include <algorithm>
#include <iostream>
#include <stack>
#include <vector>
using namespace std;
const int BMAX = 317;
const int BNUM = 316;
const int MAXN = 100010;
int b[BMAX] = {0}, a[MAXN] = {0};
stack<int> s;
void findmid() {
  int mid = (s.size() + 1) / 2, sum = 0, i, j;
  for (i = 0; i <= BMAX; ++i) {
    if (sum + b[i] >= mid) {
      break;
    }
    sum += b[i];
  }
  for (j = i * BNUM; j < MAXN; ++j) {
    sum += a[j];
    if (sum >= mid) break;
  }
  printf("%d\n", j);
  return;
}
int main() {
  int n;
  scanf("%d", &n);
  for (int i = 0; i < n; ++i) {
    char formats[11];
    int num;
    scanf("%s", formats);
    if (formats[1] == 'u') {
      scanf("%d", &num);
      s.push(num);
      ++b[num / BNUM];
      ++a[num];
    } else {
      if (s.empty()) {
        printf("Invalid\n");
      } else if (formats[1] == 'o') {
        int temp = s.top();
        s.pop();
        printf("%d\n", temp);
        --b[temp / BNUM];
        --a[temp];
      } else {
        findmid();
      }
    }
  }
  return 0;
}
