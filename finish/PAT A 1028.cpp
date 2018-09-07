#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;
const int maxn = 100001;
int n, m;
struct node {
  char name[20];
  int id, score;
} v[maxn];

bool cmp(node a, node b) {
  if (m == 1)
    return a.id < b.id;
  else if (m == 2)
    return (a.name == b.name) ? (a.id < b.id) : (strcmp(a.name, b.name) <= 0);
  else
    return (a.score == b.score) ? (a.id < b.id) : (a.score <= b.score);
}
int main(int argc, char const *argv[]) {
  node temp;
  cin >> n >> m;
  getchar();
  for (int i = 0; i < n; ++i) {
    scanf("%d %s %d", &temp.id, &temp.name, &temp.score);
    v[i] = temp;
  }
  sort(v, v + n, cmp);
  for (int i = 0; i < n; ++i) {
    temp = v[i];
    printf("%06d %s %d\n", temp.id, temp.name, temp.score);
  }
  return 0;
}
