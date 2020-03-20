#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
struct node {
  int cability;
  double price;
};
bool cmp(node a, node b) {
  return (a.price == b.price) ? (a.cability > b.cability) : (a.price > b.price);
}
int main() {
  int n, m, temp, id = 0;
  cin >> n >> m;
  getchar();
  vector<node> v(n);
  for (int i = 0; i < n; ++i) {
    cin >> v[i].cability;
  }
  getchar();
  for (int i = 0; i < n; ++i) {
    double total;
    cin >> total;
    v[i].price = total / v[i].cability;
  }
  getchar();
  sort(v.begin(), v.end(), cmp);
  double sum = 0.0;
  temp = m;
  while (temp > 0 && id < n) {
    int now = min(v[id].cability, temp);
    //		cout<<temp<<" "<<now<<" ";
    sum += now * v[id].price * 1.0;
    temp -= now;
    ++id;
    //		cout<<sum<<" "<<temp<<" "<<id<<endl;
  }
  printf("%.2f\n", sum);
  return 0;
}
