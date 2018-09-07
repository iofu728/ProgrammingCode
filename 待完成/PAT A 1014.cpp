#include <cstdio>
#include <queue>
using namespace std;

int n, m, k, q;

int currentpoint;

int main() {
  scanf("%d %d %d %d", &n, &m, &k, &q);
  int process[k];
  for (int i = 0; i < k; i++) {
    scanf("%d", &process[i]);
  }
  for (int j = 0; j < q; j++) {
    int z, x, time = 0;

    for (int i = 0; i < n; i++) {
      queue A
    }
    scanf("%d", &currentpoint);
    if (currentpoint <= n) {
      printf("08:%02d", process[currentpoint]);
    } else if (currentpoint <= n * m) {
      z = (currentpoint - 1) % n;
      x = (currentpoint - 1) / n;
      for (int i = 0; i <= x; i++) {
        time += process[i * n + z];
      }

      if (time < 60)
        printf("08:%02d\n", time);
      else if (time > 600)
        printf("Sorry\n");
      else {
        printf("%02d:%02d\n", time / 60 + 8, time % 60);
      }
    } else {
    }
  }
  return 0;
}
