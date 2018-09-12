#include <cstdio>
#include <iostream>

using namespace std;

long long gca(long long a, long long b) { return !b ? abs(a) : gca(b, a % b); }

int main(int argc, char const *argv[]) {
  long long n, a, b, suma = 0, sumb = 1, gcanum;
  cin >> n;
  for (int i = 0; i < n; ++i) {
    scanf("%lld/%lld", &a, &b);
    gcanum = gca(a, b);
    a /= gcanum;
    b /= gcanum;
    suma = b * suma + a * sumb;
    sumb = b * sumb;
    gcanum = gca(suma, sumb);
    suma /= gcanum;
    sumb /= gcanum;
  }
  long long result = suma / sumb;
  suma -= result * sumb;
  if (result) {
    printf("%lld", result);
    if (suma) printf(" ");
  }
  if (suma) printf("%lld/%lld", suma, sumb);
  if (!result && !suma) cout << '0';
  return 0;
}
