#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct node {
  string name, code;
};
bool changecode(string &str) {
  bool vis = false;
  for (int i = 0; i < str.size(); ++i) {
    char temp = str[i];
    if (temp == '0') {
      str[i] = '%';
      vis = true;
    } else if (temp == 'O') {
      str[i] = 'o';
      vis = true;
    } else if (temp == '1') {
      str[i] = '@';
      vis = true;
    } else if (temp == 'l') {
      str[i] = 'L';
      vis = true;
    }
  }
  return vis;
}
bool cmp(node a, node b) {
  return (a.name == b.name) ? (a.code < b.code) : (a.name < b.name);
}
vector<node> v;
int main(int argc, char const *argv[]) {
  int n, num = 0;
  cin >> n;
  getchar();
  for (int i = 0; i < n; ++i) {
    node temp;
    cin >> temp.name >> temp.code;
    getchar();
    ++num;
    if (changecode(temp.code)) {
      v.push_back(temp);
    }
  }
  if (v.size()) {
    cout << v.size() << endl;
    ;
    for (int i = 0; i < v.size(); ++i) {
      cout << v[i].name << " " << v[i].code << endl;
    }
  } else if (n == 1) {
    cout << "There is 1 account and no account is modified\n";
  } else {
    cout << "There are " << num << " accounts and no account is modified\n";
  }
  return 0;
}
