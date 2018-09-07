#include <iostream>
using namespace std;

int main() {
  int n, m;
  cin >> n;
  int array[n];
  for (int i = 0; i < n; ++i) {
    cin >> array[i];
  }
  getchar();
  cin >> m;
  int Array[m];
  for (int i = 0; i < m; ++i) {
    cin >> Array[i];
  }
  int p = 0, q = 0, mid = (n + m - 1) / 2, count = -1;
  bool vis = false;
  while (p < n && q < m && count < mid) {
    while (p < n && array[p] < Array[q] && count < mid) {
      ++count;
      ++p;
      vis = false;
    }
    while (q < m && Array[q] < array[p] && count < mid) {
      ++count;
      ++q;
      vis = true;
    }
  }
  if (count == mid) {
    cout << (vis ? Array[q - 1] : array[p - 1]) << endl;
    return 0;
  } else {
    while (p < n && count < mid) {
      ++count;
      if (count == mid) {
        cout << array[p] << endl;
      }
      ++p;
    }
    while (q < m && count < mid) {
      ++count;
      if (count == mid) {
        cout << Array[q] << endl;
      }
      ++q;
    }
  }
  return 0;
}
