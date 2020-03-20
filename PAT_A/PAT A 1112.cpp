/*
 * @Author: gunjianpan
 * @Date:   2019-03-08 12:55:33
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2019-03-08 14:03:35
 */

#include <cstring>
#include <iostream>
#include <map>

using namespace std;

map<char, bool> continuous, haveError, lonely;

int main(int argc, char const *argv[]) {
  int k;
  string str;
  cin >> k >> str;
  for (int i = 0; i < str.size(); ++i) {
    if (i < str.size() - (k - 1)) {
      bool tempContinous = true;
      for (int j = 1; j < k; ++j)
        if (str[i] != str[i + j]) {
          tempContinous = false;
          break;
        }
      if (tempContinous) {
        // cout << str[i] << ' ' << i << " " << tempContinous << endl;
        if (continuous.find(str[i]) == continuous.end())
          continuous[str[i]] = true;
        i += (k - 1);
        continue;
      } else
        // cout << "lonely" << str[i] << ' ' << i << " " << tempContinous <<
        // endl;
        lonely[str[i]] = false;
    } else
      lonely[str[i]] = false;
  }
  for (map<char, bool>::iterator i = continuous.begin(); i != continuous.end();
       ++i)
    if (lonely.find(i->first) == lonely.end()) {
      haveError[i->first] = true;
      cout << i->first;
    }
  cout << endl;
  for (int i = 0; i < str.size(); ++i) {
    cout << str[i];
    if (haveError.find(str[i]) != haveError.end()) {
      i += (k - 1);
    }
  }
  return 0;
}
