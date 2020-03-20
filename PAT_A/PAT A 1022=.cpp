#include <algorithm>
#include <iostream>
#include <map>
#include <set>
using namespace std;
int n, m;
map<string, set<int> > titles, authors, publishs, years, keys;

void input(map<string, set<int> > &mmp, string &str) {
  if (mmp.find(str) == mmp.end()) {
    cout << "Not Found\n";
  } else {
    for (auto it = mmp[str].begin(); it != mmp[str].end(); ++it) {
      printf("%07d\n", *it);
    }
  }
}
int main() {
  scanf("%d", &n);
  for (int i = 0; i < n; ++i) {
    string title, author, key, publish, year;
    int id;
    scanf("%d\n", &id);
    getline(cin, title);
    getline(cin, author);
    while (cin >> key) {
      keys[key].insert(id);
      char c = getchar();
      if (c == '\n') break;
    }
    getline(cin, publish);
    getline(cin, year);
    titles[title].insert(id);
    authors[author].insert(id);
    publishs[publish].insert(id);
    years[year].insert(id);
  }
  int num;
  scanf("%d", &m);
  for (int i = 0; i < m; ++i) {
    scanf("%d: ", &num);
    string str;
    getline(cin, str);
    cout << num << ": " << str << endl;
    switch (num) {
      case 1:
        input(titles, str);
        break;
      case 2:
        input(authors, str);
        break;
      case 3:
        input(keys, str);
        break;
      case 4:
        input(publishs, str);
        break;
      case 5:
        input(years, str);
        break;
    }
  }
  return 0;
}
