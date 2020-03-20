#include <iostream>

using namespace std;

string num[10] = {"ling", "yi",  "er", "san", "si",
                  "wu",   "liu", "qi", "ba",  "jiu"};
string unit[6] = {"Qian", "", "Shi", "Bai"};
string units[3] = {"", "Wan", "Yi"};

int main(int argc, char const *argv[]) {
  string str;
  bool havezero = false;
  bool havenum = true;
  getline(cin, str);
  if (str[0] == '-') {
    str = str.substr(1);
    cout << "Fu ";
  }
  while (str[0] == '0') str = str.substr(1);
  if (!str.length()) {
    cout << "ling";
    return 0;
  }
  int totallength = str.length();
  while (str.length()) {
    int length = str.length();
    if (str[0] != '0') {
      if (havezero) cout << " ling";
      if (totallength != length) cout << ' ';
      cout << num[str[0] - '0'];
      if (length % 4 != 1) cout << ' ' << unit[length % 4];
      havenum = true;
    } else {
      havezero = true;
    }
    if (length == 9 || length == 5) {
      if (havenum) {
        cout << ' ' << units[length / 4];
        havezero = false;
      }
      havenum = false;
    }
    str = str.substr(1);
  }

  return 0;
}
