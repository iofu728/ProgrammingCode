#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

struct node {
  int weight, idorigin, rank;
};
bool cmporigin(node a, node b) { return a.idorigin < b.idorigin; }
bool cmpweight(node a, node b) { return a.weight > b.weight; }
int main() {
  int np, ng, id;
  scanf("%d %d", &np, &ng);
  vector<node> v(np), x, y, z;  // z遍历列
  for (int i = 0; i < np; ++i) {
    scanf("%d", &v[i].weight);
    v[i].idorigin = i;
  }
  for (int i = 0; i < np; ++i) {
    scanf("%d", &id);
    z.push_back(v[id]);
  }
  //	for(int i=0;i<z.size();++i){
  //		cout<<z[i].idorigin<<' '<<z[i].weight<<endl;
  //	}
  //分组选优模拟
  while (z.size() > ng) {
    x.clear();
    int postrank = (z.size() - 1) / ng + 2;
    //		cout<<' '<<postrank<<endl;
    //每组选择
    for (int i = 0; i < z.size(); i = i + ng) {
      vector<node> temp;
      temp.insert(
          temp.begin(), z.begin() + i,
          (z.end() >= (z.begin() + i + ng)) ? (z.begin() + i + ng) : (z.end()));
      sort(temp.begin(), temp.end(), cmpweight);
      x.push_back(temp[0]);
      //			cout<<"***"<<temp[0].weight<<'
      //'<<temp[0].idorigin<<endl;
      for (int j = 1; j < temp.size(); ++j) {
        temp[j].rank = postrank;
        //				cout<<"###"<<temp[j].weight<<'
        //'<<temp[j].idorigin<<' '<<temp[j].rank<<endl;
        y.push_back(temp[j]);
      }
    }
    z = x;
  }
  sort(z.begin(), z.end(), cmpweight);
  z[0].rank = 1;
  y.push_back(z[0]);
  for (int i = 1; i < z.size(); ++i) {
    z[i].rank = 2;
    //		cout<<"$"<<z[i].weight<<' '<<z[i].idorigin<<'
    //'<<z[i].rank<<endl;
    y.push_back(z[i]);
  }
  sort(y.begin(), y.end(), cmporigin);
  for (int i = 0; i < np - 1; ++i) {
    printf("%d ", y[i].rank);
  }
  printf("%d", y[np - 1].rank);
}
