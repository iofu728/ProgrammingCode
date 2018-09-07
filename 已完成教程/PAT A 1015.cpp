#include <cmath>
#include <iostream>
using namespace std;

bool primes(int num) {
  if (num <= 1)
    return false;
  else {
    int sqr = int(sqrt(num * 1.0));
    for (int i = 2; i <= sqr; i++) {
      if (num % i == 0) return false;
    }
    return true;
  }
}
int change(int num, int D) {
  int len = 0, cha[20], changes = 0;
  do {
    cha[len++] = num % D;
    num = num / D;
  } while (num != 0);
  for (int i = 0; i < len; ++i) {
    changes = changes * D + cha[i];
  }
  return changes;
}
int main() {
  int n, m;
  while (scanf("%d", &n) != EOF) {
    if (n < 0) break;
    scanf("%d\n", &m);
    if (primes(n) == false) {
      cout << "No\n";
      continue;
    }
    cout << (primes(change(n, m)) ? "Yes\n" : "No\n");
  }
  return 0;
}
