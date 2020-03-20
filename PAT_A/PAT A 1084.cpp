/*
 * @Author: gunjianpan
 * @Date:   2018-09-13 19:25:17
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2018-09-13 19:31:46
 */
#include <iostream>

using namespace std;

int main(int argc, char const *argv[]) {
  string str1, str2, result;
  cin >> str1 >> str2;
  for (int i = 0; i < str1.size(); ++i) {
    if (str2.find(str1[i]) == string::npos &&
        result.find(toupper(str1[i])) == string::npos) {
      result += toupper(str1[i]);
    }
  }
  cout << result;
  return 0;
}
