/*
 * @Author: gunjianpan
 * @Date:   2018-09-17 13:27:18
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2018-09-17 13:59:05
 */
#include <algorithm>
#include <cmath>
#include <iostream>

using namespace std;

const int MANX = 100010;

struct node {
  int id, next, key, weight = 2 * MANX;
} v[MANX];

bool vis[MANX] = {false};

bool deweight(node a, node b) { return a.weight < b.weight; }

int main(int argc, char const *argv[]) {
  int start, n, temp, pick1 = 0, pick2 = 0;
  cin >> start >> n;
  for (int i = 0; i < n; ++i) {
    cin >> temp;
    v[temp].id = temp;
    cin >> v[temp].key >> v[temp].next;
  }
  temp = start;
  for (int i = 0; temp != -1 && i < n; ++i) {
    if (!vis[abs(v[temp].key)]) {
      v[temp].weight = pick1++;
      vis[abs(v[temp].key)] = true;
    } else {
      v[temp].weight = MANX + pick2++;
    }
    temp = v[temp].next;
  }
  sort(v, v + MANX, deweight);
  for (int i = 0; i < pick2 + pick1; ++i) {
    printf("%05d ", v[i].id);
    cout << v[i].key << ' ';
    if (i == pick1 - 1 || i == pick1 + pick2 - 1)
      cout << "-1" << endl;
    else
      printf("%05d\n", v[i + 1].id);
  }
  return 0;
}
