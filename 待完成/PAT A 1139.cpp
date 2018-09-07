#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

struct node {
  int a;
  int b;
};

vector<node> both;
vector<int> man[301], woman[301];

int n, m, o, countm = 0, countw = 0;

int findman(int num) {
  for (int i = 0; i < countm; ++i) {
    if (man[i][0] == num) return i;
  }
  return 500;
}
int findwoman(int num) {
  for (int i = 0; i < countw; ++i) {
    if (woman[i][0] == num) return i;
  }
  return 500;
}
int ffindman(int mm, int num) {
  if (mm == 500)
    return 500;
  else {
    for (int i = 1; i < man[mm].size(); ++i) {
      if (man[mm][i] == num) return i;
    }
    return 500;
  }
}
int ffindwoman(int ww, int num) {
  if (ww == 500)
    return 500;
  else {
    for (int i = 1; i < woman[ww].size(); ++i) {
      if (woman[ww][i] == num) return i;
    }
    return 500;
  }
}
bool cmp(node xx, node yy) {
  if (xx.a != yy.a) return xx.a < yy.a;
  return xx.b < yy.b;
}

int main() {
  cin >> n >> m;
  for (int i = 0; i < m; ++i) {
    int x, y;
    cin >> x >> y;
    node temp;
    if (x * y < 0) {
      if (x < 0) {
        swap(x, y);
      }
      temp.a = x;
      temp.b = -y;
      both.push_back(temp);
    } else if (x < 0) {
      if (findwoman(-x) != 500) {
        woman[findwoman(-x)].push_back(-y);
      } else {
        woman[countw].push_back(-x);
        woman[countw].push_back(-y);
        ++countw;
      }
      if (findwoman(-y) != 500) {
        woman[findwoman(-y)].push_back(-x);
      } else {
        woman[countw].push_back(-y);
        woman[countw].push_back(-x);
        ++countw;
      }
    } else {
      if (findman(x) != 500) {
        man[findman(x)].push_back(y);
      } else {
        man[countm].push_back(x);
        man[countm].push_back(y);
        ++countm;
      }
      if (findman(y) != 500) {
        man[findman(y)].push_back(x);
      } else {
        man[countm].push_back(y);
        man[countm].push_back(x);
        ++countm;
      }
    }
  }
  /*for(int i=0;i<both.size();++i){
          cout<<both[i].a<<" "<<both[i].b<<endl;
  }
  for(int i=0;i<countm;++i){
          for(int j=0;j<man[i].size();++j){
                  cout<<man[i][j]<<" ";
          }
          cout<<endl;
  }
  for(int i=0;i<countw;++i){
          for(int j=0;j<woman[i].size();++j){
                  cout<<woman[i][j]<<" ";
          }
          cout<<endl;
  }*/
  cin >> o;
  for (int i = 0; i < o; ++i) {
    int star, end;
    vector<node> connect;
    cin >> star >> end;
    if (star * end < 0) {
      int starr = star;
      if (star < 0) swap(star, end);
      int mm = findman(star), ww = findwoman(-end);
      for (int j = 0; j < both.size(); ++j) {
        node temp = both[j];
        if (ffindman(mm, temp.a) != 500 && ffindwoman(ww, temp.b) != 500) {
          if (starr < 0) {
            swap(temp.a, temp.b);
          }
          connect.push_back(temp);
        }
      }

    } else if (star < 0) {
      int ww1 = findwoman(-star), ww2 = findwoman(-end);
      for (int j = 1; j < woman[ww1].size(); ++j) {
        for (int k = 1; k < woman[ww2].size(); ++k) {
          if (ffindwoman(findwoman(woman[ww1][j]), woman[ww2][k]) != 500 &&
              woman[ww1][j] != woman[ww2][k]) {
            node temp;
            temp.a = woman[ww1][j];
            temp.b = woman[ww2][k];
            connect.push_back(temp);
          }
        }
      }
    } else {
      int mm1 = findman(star), mm2 = findman(end);
      for (int j = 1; j < man[mm1].size(); ++j) {
        for (int k = 1; k < man[mm2].size(); ++k) {
                                        if(ffindman(findman(man[mm1][j]),man[mm2][k])!=500&&man[mm1]/.//[j]!=man[mm2][k]){
						node temp;
						temp.a=man[mm1][j];
						temp.b=man[mm2][k];
						connect.push_back(temp);
        }
      }
    }
  }
  sort(connect.begin(), connect.end(), cmp);
  cout << connect.size() << endl;
  for (int j = 0; j < connect.size(); ++j) {
    node temp = connect[j];
    printf("%04d %04d\n", temp.a, temp.b);
    // cout<<temp.a<<" "<<temp.b<<endl;
  }
}
return 0;
}
