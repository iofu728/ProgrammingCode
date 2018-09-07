#include <algorithm>
#include <iostream>
using namespace std;
const int maxn = 100001;
int tempid, money[maxn];
bool tempvis = false;
void search(int left, int right, int wait) {
  if (left > right) return;
  int mid = (left + right) / 2;
  if (money[mid] == wait) {
    if (tempid != mid) {
      tempvis = true;
    }
    return;
  } else if (money[mid] > wait) {
    search(left, mid - 1, wait);
  } else {
    search(mid + 1, right, wait);
  }
}
int main() {
  int n, m;
  bool vis = false;
  scanf("%d %d", &n, &m);
  for (int i = 0; i < n; ++i) {
    scanf("%d", &money[i]);
  }
  sort(money, money + n);
  for (int i = 0; i < n; ++i) {
    tempvis = false;
    tempid = i;
    if (money[i] >= m) {
      break;
    } else {
      search(0, n - 1, m - money[i]);
      if (tempvis) {
        vis = true;
        printf("%d %d", money[i], m - money[i]);
        return 0;
      }
    }
  }
  if (!vis) printf("No Solution");
  return 0;
}
