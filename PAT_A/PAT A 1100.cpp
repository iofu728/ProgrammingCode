/*
 * @Author: gunjianpan
 * @Date:   2018-09-17 14:33:40
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2018-09-17 18:26:05
 */
#include <cstdlib>
#include <iostream>
#include <map>

using namespace std;

const string word[13] = {"tret", "jan", "feb", "mar", "apr", "may", "jun",
                         "jly",  "aug", "sep", "oct", "nov", "dec"};
const string digit[13] = {"",    "tam", "hel", "maa", "huh", "tou", "kes",
                          "hei", "elo", "syy", "lok", "mer", "jou"};
std::map<string, int> wordmap;
std::map<string, int> digitmap;

int main(int argc, char const *argv[]) {
  for (int i = 0; i < 13; ++i) {
    wordmap[word[i]] = i;
    digitmap[digit[i]] = i;
  }
  int n, num = 0;
  string str;
  cin >> n;
  getchar();
  for (int i = 0; i < n; ++i) {
    getline(cin, str);
    if (isdigit(str[0])) {
      num = atoi(str.c_str());
      if (num / 13) {
        cout << digit[num / 13];
        if (num % 13) cout << ' ' << word[num % 13];
      } else
        cout << word[num % 13];
    } else {
      if (str.size() == 4)
        cout << 0;
      else if (str.size() == 3)
        cout << digitmap[str] * 13 + wordmap[str];
      else
        cout << digitmap[str.substr(0, 3)] * 13 + wordmap[str.substr(4)];
    }
    cout << endl;
  }

  return 0;
}
