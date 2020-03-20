#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int waittime = 0;
struct node {
  int come, spend;
};
struct win {
  int poptime, endtime;
};
int n, k;
bool cmp(node a, node b) { return a.come < b.come; }
int main() {
  scanf("%d %d\n", &n, &k);
  vector<int> window(k);
  fill(window.begin(), window.end(), 0);
  vector<node> v;
  for (int i = 0; i < n; ++i) {
    node temp;
    int hour, minute, second;
    scanf("%d:%d:%d %d", &hour, &minute, &second, &temp.spend);
    temp.come = ((hour - 8) * 60 + minute) * 60 + second;
    if (temp.come <= 32400) v.push_back(temp);
  }
  sort(v.begin(), v.end(), cmp);
  //	for(int i=0;i<v.size();++i){
  //		cout<<v[i].come<<" "<<v[i].spend<<endl;
  //	}
  for (int i = 0; i < v.size(); i++) {
    sort(window.begin(), window.end());
    if (window[0] > v[i].come) {
      waittime += (window[0] - v[i].come);
      window[0] += v[i].spend * 60;
    } else {
      window[0] = v[i].come + v[i].spend * 60;
    }

    //		for(int i=0;i<3;++i){
    //			cout<<window[i]<<" ";
    //		}
    //		cout<<waittime<<endl;
  }

  if (v.size() == 0)
    cout << "0.0\n";
  else {
    printf("%.1f\n", (waittime / (60.0 * v.size())));
  }
  return 0;
}
