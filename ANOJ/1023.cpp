#include <algorithm>
#include <iostream>
using namespace std;

int main() {
  long long num;
  int n;
  scanf("%d", &n);
  int s[n];
  for (int i = 0; i < n; ++i) {
    scanf("%lld", &num);
    if (num > 0 && num <= n) {
      s[num - 1] = 2;
    }
  }
  for (int i = 0; i < n; ++i) {
    if (s[i] != 2) {
      cout << i + 1 << endl;
      break;
    }
  }
  return 0;
}
