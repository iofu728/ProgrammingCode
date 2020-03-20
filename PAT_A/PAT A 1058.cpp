#include <iostream>
using namespace std;
int main() {
  int g1, g2, g3, s1, s2, s3, k1, k2, k3, vis = 0;
  scanf("%d.%d.%d %d.%d.%d", &g1, &s1, &k1, &g2, &s2, &k2);
  k3 = (k2 + k1) % 29;
  vis = (k2 + k1) / 29;
  s3 = (s2 + s1 + vis) % 17;
  vis = (s2 + s1 + vis) / 17;
  g3 = (g1 + g2 + vis);
  printf("%d.%d.%d\n", g3, s3, k3);
  return 0;
}
