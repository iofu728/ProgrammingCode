#include <iostream>

using namespace std;

const int MAXN = 10009;
bool vis[MAXN] = {false};
int n;

bool isPrimer(int num) {
  if (num == 1) {
    return false;
  }
  for (int i = 2; i * i <= num; ++i) {
    if (!(num % i)) return false;
  }
  return true;
}

void haveEmpty(int node) {
  for (int i = 0; i < n; ++i) {
    int pos = (node + i * i) % n;
    if (!vis[pos]) {
      cout << pos % n;
      vis[pos] = true;
      return;
    }
  }
  cout << '-';
}

int main(int argc, char const *argv[]) {
  int m, temp;
  cin >> n >> m;
  while (!isPrimer(n)) ++n;
  for (int i = 0; i < m; ++i) {
    cin >> temp;
    if (i) cout << ' ';
    haveEmpty(temp);
  }
  return 0;
}
