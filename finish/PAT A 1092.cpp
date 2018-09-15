#include <iostream>

using namespace std;

int vis[300];

int main(int argc, char const *argv[]) {
  string a, b;
  cin >> a >> b;
  int result = 0;
  for (int i = 0; i < a.size(); ++i) ++vis[a[i]];
  for (int i = 0; i < b.size(); ++i) {
    if (vis[b[i]] > 0) {
      --vis[b[i]];
    } else {
      ++result;
    }
  }
  if (result) {
    cout << "No " << result;
  } else {
    cout << "Yes " << a.size() - b.size();
  }

  return 0;
}
