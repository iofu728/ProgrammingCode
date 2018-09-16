/*
 * @Author: gunjianpan
 * @Date:   2018-09-16 09:14:25
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2018-09-16 09:50:21
 */
#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

struct node {
  string id;
  int flag = 0, time;
};

bool compareinandout(node a, node b) {
  return a.id == b.id ? a.time < b.time : a.id < b.id;
}

bool comparecar(node a, node b) { return a.time < b.time; }

int main(int argc, char const *argv[]) {
  int n, m, hh, mm, ss, maxtime = -1, tempindex = 0;
  cin >> n >> m;
  string inorout;
  std::vector<node> v, car;
  std::vector<int> havecar(n);
  for (int i = 0; i < n; ++i) {
    node temp;
    cin >> temp.id;
    scanf("%d:%d:%d", &hh, &mm, &ss);
    cin >> inorout;
    temp.time = hh * 3600 + mm * 60 + ss;
    temp.flag = inorout == "in" ? 1 : -1;
    v.push_back(temp);
  }
  sort(v.begin(), v.end(), compareinandout);
  map<string, int> stad;
  for (int i = 0; i < n - 1; ++i) {
    if (v[i].flag == 1 && v[i + 1].flag == -1 && v[i].id == v[i + 1].id) {
      car.push_back(v[i]);
      car.push_back(v[i + 1]);
      stad[v[i].id] += (v[i + 1].time - v[i].time);
      if (stad[v[i].id] > maxtime) maxtime = stad[v[i].id];
    }
  }
  sort(car.begin(), car.end(), comparecar);
  for (int i = 0; i < car.size(); ++i) {
    if (!i) {
      havecar[i] = car[i].flag;
    } else {
      havecar[i] = havecar[i - 1] + car[i].flag;
    }
  }
  for (int i = 0; i < m; ++i) {
    scanf("%d:%d:%d", &hh, &mm, &ss);
    int temptime = hh * 3600 + mm * 60 + ss, j;
    for (j = tempindex; j < car.size(); ++j) {
      if (car[j].time > temptime) {
        cout << havecar[j - 1] << endl;
        break;
      } else if (j == car.size() - 1) {
        cout << havecar[j] << endl;
      }
    }
    tempindex = j;
  }

  for (map<string, int>::iterator it = stad.begin(); it != stad.end(); ++it) {
    if (it->second == maxtime) cout << it->first << ' ';
  }
  printf("%02d:%02d:%02d", maxtime / 3600, (maxtime % 3600) / 60, maxtime % 60);

  return 0;
}
