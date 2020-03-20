#include <algorithm>
#include <cstdio>
#include <iostream>
#include <queue>
using namespace std;
const int IINF = -0x3fffffff;

int star, ed, flam;
int getmaxsum(int A[], int n) {
  int sum = 0;
  int max = 0;
  bool zero = false;
  star = 0;
  ed = 0;
  flam = 0;
  for (int i = 0; i < n; i++) {
    sum += A[i];
    if (!A[i]) zero = true;
    if (sum >= 0) {
      if (max < sum) {
        max = sum;
        ed = i;
        star = flam;
      }
    } else {
      sum = 0;
      flam = i + 1;
    }
  }
  if (ed == 0 && A[0] <= 0) {
    if (zero == true) {
      max = IINF;

      for (int i = 0; i < n; i++) {
        if (A[i] > max) {
          max = A[i];
          star = i;
          ed = i;
        }
      }
    } else {
      max = 0;
      star = 0;
      ed = n - 1;
    }
  }

  return max;
}

int main() {
  int n;
  scanf("%d", &n);
  int num[n];
  for (int i = 0; i < n; i++) {
    scanf("%d", &num[i]);
  }
  getmaxsum(num, n);
  printf("%d %d %d", getmaxsum(num, n), num[star], num[ed]);
}
