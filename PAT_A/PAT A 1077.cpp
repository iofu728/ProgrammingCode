#include <algorithm>
#include <iostream>

using namespace std;

int main(int argc, char const *argv[]) {
  int n;
  cin >> n;
  getchar();
  string common;
  for (int i = 0; i < n; ++i) {
    string s;
    getline(cin, s);
    reverse(s.begin(), s.end());
    if (i) {
      int length = min(s.length(), common.length());
      for (int j = 0; j < length; ++j) {
        if (common[j] != s[j]) {
          common = common.substr(0, j);
          break;
        }
      }
    } else {
      common = s;
    }
  }
  reverse(common.begin(), common.end());
  if (!common.length()) common = "nai";
  cout << common;
  return 0;
}
