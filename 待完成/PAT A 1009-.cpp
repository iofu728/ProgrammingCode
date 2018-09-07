#include <cstdio>

const int K = 10;
const int N = 1000;
int main() {
  double a[N] = {0}, b[N] = {0}, c[N] = {0};
  int n, m, e, f, num = 0;
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d %lf", &e, &a[e]);
  }
  scanf("%d", &m);
  for (int i = 0; i < m; i++) {
    scanf("%d %lf", &f, &b[f]);
  }
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (a[i] && b[j]) {
        c[i + j] += a[i] * b[j];
      }
    }
  }
  for (int i = 0; i < N; i++) {
    if (c[i]) num++;
  }
  printf("%d", num);
  for (int i = 0; i < N; i++) {
    if (c[i]) {
      printf(" %d %.2lf", i, c[i]);
    }
  }
  return 0;
}
