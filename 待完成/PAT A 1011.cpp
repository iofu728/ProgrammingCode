#include <algorithm>
#include <cstdio>
using namespace std;
int main() {
  char max[3] = {'W', 'T', 'L'};
  double maxa = 0, maxb = 0, maxc = 0;
  int a, b, c;
  double A[3], B[3], C[3];

  scanf("%lf %lf %lf", &A[0], &A[1], &A[2]);
  scanf("%lf %lf %lf", &B[0], &B[1], &B[2]);
  scanf("%lf %lf %lf", &C[0], &C[1], &C[2]);

  for (int i = 0; i < 3; i++) {
    if (A[i] > maxa) {
      maxa = A[i];
      a = i;
    }
    if (B[i] > maxb) {
      maxb = B[i];
      b = i;
    }
    if (C[i] > maxc) {
      maxc = C[i];
      c = i;
    }
  }
  sort(A, A + 3);
  sort(B, B + 3);
  sort(C, C + 3);
  printf("%c %c %c ", max[a], max[b], max[c]);
  printf("%.2lf", (A[2] * B[2] * C[2] * 0.65 - 1) * 2);

  return 0;
}
