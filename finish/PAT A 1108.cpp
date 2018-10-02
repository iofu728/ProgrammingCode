/*
 * @Author: gunjianpan
 * @Date:   2018-10-01 23:27:18
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2018-10-02 13:43:57
 */
#include <cstring>
#include <iostream>

using namespace std;

int main(int argc, char const *argv[]) {
  int n, cnt = 0;
  char a[50], b[50];
  double temp, sum = 0.0;
  cin >> n;
  for (int i = 0; i < n; ++i) {
    scanf("%s", a);
    sscanf(a, "%lf", &temp);
    sprintf(b, "%.2lf", temp);
    int flag = 0;
    for (int j = 0; j < strlen(a); j++)
      if (a[j] != b[j]) flag = 1;
    if (flag || temp < -1000 || temp > 1000) {
      printf("ERROR: %s is not a legal number\n", a);
    } else {
      sum += temp;
      ++cnt;
    }
  }
  if (!cnt)
    printf("The average of 0 numbers is Undefined");
  else if (cnt == 1)
    printf("The average of 1 number is %.2lf", sum);
  else
    printf("The average of %d numbers is %.2lf", cnt, sum / cnt);
  return 0;
}
