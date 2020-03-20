/*
 * @Author: gunjianpan
 * @Date:   2018-09-14 11:16:44
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2018-09-14 20:16:51
 */
#include <cstdio>
#include <iostream>

using namespace std;

long long gcd(long long a, long long b) { return !b ? abs(a) : gcd(b, a % b); }

string operation = "+-*/";

void printfsimple(long long a, long long b) {
  if (!b) {
    cout << "Inf";
    return;
  }
  if (!a) {
    cout << '0';
    return;
  }
  string result;
  if (a < 0) {
    a *= -1;
    result += "(-";
  } else if (b < 0) {
    b *= -1;
    result += "(-";
  }
  if (a >= b) {
    result += std::to_string(a / b);
    if (b != 1) result += ' ';
    a -= b * (a / b);
  }
  cout << result;
  if (a) cout << a;
  if (b != 1) cout << '/' << b;
  if (result[0] == '(') cout << ')';
}

int main(int argc, char const *argv[]) {
  long long a, b, c, d, e = 0, f = 0, gcdvalue;
  scanf("%lld/%lld %lld/%lld", &a, &b, &c, &d);
  gcdvalue = gcd(a, b);
  a /= gcdvalue;
  b /= gcdvalue;
  gcdvalue = gcd(c, d);
  c /= gcdvalue;
  d /= gcdvalue;
  for (int i = 0; i < 4; ++i) {
    printfsimple(a, b);
    cout << ' ' << operation[i] << ' ';
    printfsimple(c, d);
    cout << ' ' << '=' << ' ';
    if (!i) {
      e = a * d + c * b;
      f = d * b;
    } else if (i == 1) {
      e = a * d - c * b;
      f = d * b;
    } else if (i == 2) {
      e = a * c;
      f = d * b;
    } else {
      e = a * d;
      f = c * b;
    }
    gcdvalue = gcd(e, f);
    e /= gcdvalue;
    f /= gcdvalue;
    printfsimple(e, f);
    cout << endl;
  }

  return 0;
}
