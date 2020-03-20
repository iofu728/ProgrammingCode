#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>

using namespace std;

int main() {
  string sce;
  cin >> sce;
  if (sce[0] == '-') cout << '-';
  int pos = sce.find('E');
  int power = atoi(sce.substr(pos + 2).c_str());
  if (sce[pos + 1] == '-') {
    if (!power) {
      for (int i = 1; i < pos; ++i) {
        if (i == 2) cout << '.';
        if (isdigit(sce[i])) cout << sce[i];
      }
    } else {
      cout << "0.";
      for (int i = 1; i < power; ++i) cout << '0';
      for (int i = 1; i < pos; ++i) {
        if (isdigit(sce[i])) cout << sce[i];
      }
    }
  } else {
    if (pos - 3 < power) {
      if (sce[1] != '0') cout << sce[1];
      for (int i = 3; i < pos; ++i) {
        if (isdigit(sce[i])) cout << sce[i];
      }
      for (int i = 0; i < power - (pos - 3); ++i) cout << '0';
    } else {
      if (sce[1] != '0') cout << sce[1];
      for (int i = 3; i < pos; ++i) {
        if (i == 3 + power) cout << '.';
        if (isdigit(sce[i])) cout << sce[i];
      }
    }
  }
  return 0;
}
