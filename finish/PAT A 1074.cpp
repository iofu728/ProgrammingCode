#include <cstdio>
#include <iostream>

using namespace std;

int main(int argc, char const *argv[]) {
  int begin, n, k, id, t = 0;
  int num[100009], next[100009], list[100009], rever[100009];
  cin >> begin >> n >> k;
  for (int i = 0; i < n; ++i) {
    cin >> id;
    cin >> num[id] >> next[id];
  }
  while (begin != -1) {
    list[t++] = begin;
    begin = next[begin];
  }

  for (int i = 0; i < t; ++i) rever[i] = list[i];
  /* every K num，reverse */
  for (int i = 0; i < t - t % k; ++i) {
    rever[i] = list[(i / k + 1) * k - 1 - i % k];
    /* find No.j block end = (i/k+1)*k-1 */
  }
  for (int i = 0; i < t - 1; ++i)
    printf("%05d %d %05d\n", rever[i], num[rever[i]], rever[i + 1]);
  printf("%05d %d -1", rever[t - 1], num[rever[t - 1]]);
  return 0;
}
