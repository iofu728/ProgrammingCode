#include <iostream>
#include <string>
using namespace std;
int main(int argc, char const *argv[]) {
  string str;
  cin >> str;
  int size = str.size(), n = size + 2, n1 = n / 3, n2 = n1 + n % 3, n3 = n1;
  char array[n1][n2];
  for (int i = 0; i < n1 - 1; ++i) {
    array[i][0] = str[i];
    for (int j = 1; j < n2 - 1; ++j) {
      array[i][j] = ' ';
    }
    array[i][n2 - 1] = str[size - i - 1];
  }
  for (int i = 0; i < n2; ++i) {
    array[n1 - 1][i] = str[n1 + i - 1];
  }
  for (int i = 0; i < n1; ++i) {
    for (int j = 0; j < n2; ++j) {
      cout << array[i][j];
    }
    cout << endl;
  }

  return 0;
}
