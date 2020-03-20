#include <algorithm>
#include <cstring>
#include <iostream>
#include <vector>
using namespace std;
struct node {
  char name[9];
  int age, worth;
};
bool cmp(node a, node b) {
  if (a.worth != b.worth) {
    return a.worth > b.worth;
  } else if (a.age != b.age) {
    return a.age < b.age;
  } else {
    return (strcmp(a.name, b.name) < 0);
  }
}
int main() {
  int n, k;
  scanf("%d %d", &n, &k);
  vector<node> v;
  for (int i = 0; i < n; ++i) {
    node temp;
    scanf("%s %d %d", temp.name, &temp.age, &temp.worth);
    v.push_back(temp);
  }
  sort(v.begin(), v.end(), cmp);
  for (int i = 0; i < k; ++i) {
    int m, amin, amax, num = 0;
    scanf("%d %d %d", &m, &amin, &amax);
    printf("Case #%d:\n", i + 1);
    for (int j = 0; j < v.size() && num < m; ++j) {
      node temp = v[j];
      if (temp.age >= amin && temp.age <= amax) {
        printf("%s %d %d\n", temp.name, temp.age, temp.worth);
        ++num;
      }
    }
    if (!num) {
      printf("None\n");
    }
  }
  return 0;
}
