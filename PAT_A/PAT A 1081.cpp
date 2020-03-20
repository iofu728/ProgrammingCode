#include <cstdio>
#include <iostream>

using namespace std;

long long gcd(long long a, long long b) { return !b ? abs(a) : gcd(b, a % b); }

int main(int argc, char const *argv[]) {
  long long n, a, b, suma = 0, sumb = 1, gcdnum;
  cin >> n;
  for (int i = 0; i < n; ++i) {
    scanf("%lld/%lld", &a, &b);
    gcdnum = gcd(a, b);
    a /= gcdnum;
    b /= gcdnum;
    suma = b * suma + a * sumb;
    sumb = b * sumb;
    gcdnum = gcd(suma, sumb);
    suma /= gcdnum;
    sumb /= gcdnum;
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
