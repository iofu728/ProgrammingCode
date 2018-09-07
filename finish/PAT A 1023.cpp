#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
vector<int> v, t, p;
bool vis[11] = {false};
void string2vector(string str) {
  int constvis = false;
  for (int i = 0; i < str.size(); ++i) {
    int temp = str[i] - '0';
    if (temp != 0) constvis = true;
    if (constvis == false && i != (str.size() - 1)) {
    } else {
      p.push_back(temp);
    }
  }
  for (int i = p.size() - 1; i >= 0; --i) {
    v.push_back(p[i]);
    vis[p[i]] = true;
  }
  return;
}
bool doublenum() {
  int other = 0;
  bool constvis = true;
  for (int i = 0; i < v.size(); ++i) {
    int temp = v[i] * 2 + other;
    other = temp / 10;
    t.push_back(temp % 10);
    if (vis[temp % 10] == false && constvis == true) constvis = false;
  }
  if (other != 0) {
    t.push_back(other);
    if (vis[other] == false) constvis = false;
  }
  return constvis;
}
int main() {
  string str;
  fill(vis, vis + 11, false);
  cin >> str;
  string2vector(str);
  //	for(int i=v.size()-1;i>=0;--i){
  //		cout<<v[i];
  //	}
  //	cout<<endl;
  bool temp = doublenum();
  if (temp == false)
    cout << "No\n";
  else
    cout << "Yes\n";
  int vis = false;
  for (int i = t.size() - 1; i >= 0; --i) {
    cout << t[i];
  }
  cout << endl;
  return 0;
}
