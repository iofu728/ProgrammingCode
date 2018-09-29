/*
 * @Author: gunjianpan
 * @Date:   2018-09-29 16:08:29
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2018-09-29 19:20:05
 */
#include <iostream>

using namespace std;

int main(int argc, char const *argv[]) {
  string s;
  int a, b, c, d;
  cin >> a >> b >> c >> d;
  getchar();
  while (getline(cin, s)) {
    int c1, c2, p1, p2;
    for (int i = 0; i < s.size() - 1; i += 2) {
      p1 = s[i] - 'a';
      p2 = s[i + 1] - 'a';
      c1 = p1 * a + p2 * c;
      c2 = p1 * b + p2 * d;
      c1 = c1 % 26;
      c2 = c2 % 26;
      cout << (char)(c1 + 'A') << (char)(c2 + 'A');
    }
    cout << endl;
  }
  return 0;
}
