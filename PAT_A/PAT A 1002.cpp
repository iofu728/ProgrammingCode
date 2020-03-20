#include <cstdio>

int main() {
  int a, b, d, e = 0;
  double c[1001] = {0}, f[1001] = {0}, g[1001] = {0};
  scanf("%d", &a);
  for (int i = 0; i < a; i++) {
    scanf("%d ", &d);
    scanf("%lf", &c[d]);
  }
  scanf("%d", &b);
  for (int i = 0; i < b; i++) {
    scanf("%d ", &d);
    scanf("%lf", &f[d]);
  }
  for (int i = 0; i < 1001; i++) {
    g[i] = c[i] + f[i];
    if (g[i]) e++;
  }
  printf("%d", e);
  for (int i = 1000; i >= 0; i--) {
    if (g[i]) {
      printf(" %d %.1lf", i, g[i]);
    }
  }
  return 0;
}
