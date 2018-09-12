#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

struct node {
  string name, id;
  int grade;
};

bool comparenode(node a, node b) { return a.grade > b.grade; }

int main(int argc, char const *argv[]) {
  int n, start, end;
  cin >> n;
  std::vector<node> v, u;
  for (int i = 0; i < n; ++i) {
    node temp;
    cin >> temp.name >> temp.id >> temp.grade;
    v.push_back(temp);
  }
  cin >> start >> end;
  if (start > end) swap(start, end);
  for (int i = 0; i < n; ++i) {
    if (v[i].grade <= end && v[i].grade >= start) u.push_back(v[i]);
  }
  if (!u.size()) {
    cout << "NONE";
  } else {
    sort(u.begin(), u.end(), comparenode);
    for (int i = 0; i < u.size(); ++i)
      cout << u[i].name << ' ' << u[i].id << endl;
  }
  return 0;
}
