#include <iostream>
#include <string>
using namespace std;
int n;
string digital(string s, int *e) {
  while (s.length() > 0 && s[0] == '0') {
    s.erase(s.begin());
  }
  int p = s.find('.');
  if (p == string::npos) {
    *e = s.length();
  } else if (p == 0) {
    s.erase(s.begin());
    while (s.length() > 0 && s[0] == '0') {
      s.erase(s.begin());
      --(*e);
    }
  } else {
    *e = p;
    s.erase(s.begin() + p);
  }
  if (!s.length()) {
    s = "0";
    *e = 0;
  }
  s = "0." + s;
  if (n + 2 <= s.length()) {
    s.erase(s.begin() + n + 2, s.end());
  } else {
    for (int i = s.length(); i < n + 2; ++i) {
      s += '0';
    }
  }
  return s;
}
int main() {
  string s1, s2;
  cin >> n >> s1 >> s2;
  int e1 = 0, e2 = 0;
  s1 = digital(s1, &e1);
  s2 = digital(s2, &e2);
  bool flog = (s1 == s2) && (e1 == e2);
  if (flog) {
    printf("YES %s*10^%d\n", s1.c_str(), e1);
  } else {
    printf("NO %s*10^%d %s*10^%d\n", s1.c_str(), e1, s2.c_str(), e2);
  }
  return 0;
}
