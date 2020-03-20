#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct node {
  string name, id;
  int grades;
};
vector<node> f, m;

bool cmpfemale(node a, node b) { return a.grades > b.grades; }
bool cmpman(node a, node b) { return a.grades < b.grades; }
int main() {
  int n, fegrade, magrade;
  cin >> n;
  getchar();
  for (int i = 0; i < n; ++i) {
    node temp;
    string gender;
    cin >> temp.name >> gender >> temp.id >> temp.grades;
    //		cout<<gender<<" "<<gender[0]<<endl;
    if (gender[0] == 'F') {
      f.push_back(temp);
    } else {
      m.push_back(temp);
    }
  }
  //	cout<<f.size()<<" "<<m.size()<<endl;
  bool vis = true;
  if (!f.size()) {
    vis = false;
    cout << "Absent\n";
  } else {
    sort(f.begin(), f.end(), cmpfemale);
    fegrade = f[0].grades;
    cout << f[0].name << " " << f[0].id << endl;
  }
  if (!m.size()) {
    vis = false;
    cout << "Absent\n";
  } else {
    sort(m.begin(), m.end(), cmpman);
    magrade = m[0].grades;
    cout << m[0].name << " " << m[0].id << endl;
  }
  if (!vis) {
    cout << "NA\n";
  } else {
    cout << (fegrade - magrade) << endl;
  }
  return 0;
}
