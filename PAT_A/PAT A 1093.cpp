#include <cstdio>
#include <cstring>
char str[100010];
const int M = 1000000007;
const int MM = 100010;
int left[MM] = {0};
int main() {
  int right = 0, ans = 0, end;
  gets(str);
  end = strlen(str);
  for (int i = 0; i < end; i++) {
    if (i > 0) {
      left[i] = left[i - 1];
    }
    if (str[i] == 'P') left[i]++;
  }

  for (int i = end - 1; i >= 0; i--) {
    if (str[i] == 'T')
      right++;
    else if (str[i] == 'A')
      ans = (ans + right * left[i]) % M;
  }

  printf("%d\n", ans);
  return 0;
}
