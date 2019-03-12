#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

bool compare(pair<int, int> a, pair<int, int> b) { return a.second > b.second; }

int main() {
  int num, dist;
  cin >> num >> dist;
  vector<pair<int, int> > banks(num, pair<int, int>(0, 0));
  int maxDist = 0, index = -1;
  for (int i = 0; i < num; i++) {
    int a, b;
    cin >> a >> b;
    if (a > maxDist) {
      maxDist = a;
      index = i;
    }
    banks[i] = pair<int, int>(a, b);
  }
  sort(banks.begin(), banks.end(), compare);
  vector<int> res(num, 0);

  int maxValue = 0;

  for (int i = 0; i < num; ++i) {
    int nowIndex = banks[i].first;
    int index = i + 1;
    while (index < num && abs(nowIndex - banks[index].first) < dist &&
           banks[i].second + banks[index].second > maxValue)  // pruning
      ++index;
    if (index == num || banks[i].second + banks[index].second < maxValue)
      continue;

    int nowValue = banks[i].second + banks[index].second;
    // cout << nowIndex << ' ' << nowValue << ' ' << banks[index].first <<
    // endl;
    if (nowValue > maxValue) maxValue = nowValue;
  }
  cout << maxValue << endl;
}
