#include <iostream>
using namespace std;

string str;
void change(int n) {
  int a = n / 13, b = n % 13;
  if (a <= 9) {
    str.push_back(a + '0');
  } else {
    str.push_back(a - 10 + 'A');
  }
  if (b <= 9) {
    str.push_back(b + '0');
  } else {
    str.push_back(b - 10 + 'A');
  }
}
int main(int argc, char const *argv[]) {
  int n, m, k;
  scanf("%d %d %d", &n, &m, &k);
  str.push_back('#');
  change(n);
  change(m);
  change(k);
  cout << str << endl;
  return 0;
}