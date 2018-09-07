#include <cstdio>
#include <cstring>
#include <vector>
char num[10][10] = {"zero", "one", "two",   "three", "four",
                    "five", "six", "seven", "eight", "night"};

void DFS(int n) {
  if (n / 10 == 0) {
    printf("%s", num[n % 10]);
    return;
  }
  DFS(n / 10);
  printf(" %s", num[n % 10]);
}
int main() {
  char n[111];
  int a, sum = 0;
  gets(n);
  int len = strlen(n);
  for (int i = 0; i < len; i++) {
    a = (n[i] - '0');
    sum += a;
  }

  DFS(sum);

  return 0;
}
