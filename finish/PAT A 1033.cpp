#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
int ability, d;
struct node {
  int start, end;
  double price;
};
struct oil {
  int dis;
  double price;
};
vector<node> v, m;
vector<oil> o;
bool cmpoilstart(oil a, oil b) {
  return (a.dis == b.dis) ? (a.price < b.price) : (a.dis < b.dis);
}
bool cmpoil(oil a, oil b) {
  return (a.price == b.price) ? (a.dis < b.dis) : (a.price < b.price);
}
bool cmpdis(node a, node b) { return a.start <= b.start; }
bool canreach() {
  sort(v.begin(), v.end(), cmpdis);
  for (int i = 1; i < v.size(); ++i) {
    if (v[i].start > v[i - 1].end) {
      return false;
    }
  }
  int endv = v.size() - 1;
  if (v[endv].end >= d) {
    return true;
  } else {
    return false;
  }
}
void margin(node temp) {
  int flag = 0;
  for (int i = 0; i < m.size(); ++i) {
    if (m[i].start <= temp.start && m[i].end >= temp.start) {
      m[i].end = temp.end;
      ++flag;
    } else if (m[i].start <= temp.end && m[i].end >= temp.end) {
      if (flag) {
        m[i].start = m[i - 1].start;
        m.erase(m.begin() + i - 1);
      } else {
        m[i].start = temp.start;
      }
      ++flag;
    }
  }
  if (!flag) m.push_back(temp);
}
bool lowprice(node temp) {
  for (int i = 1; i < v.size(); ++i) {
    if (v[i - 1].start < temp.start && v[i].start > temp.start &&
        v[i - 1].price > temp.price) {
      return true;
    }
  }
  return false;
}
bool havein(node temp) {
  for (int i = 0; i < m.size(); ++i) {
    if (m[i].start <= temp.start && m[i].end >= temp.end) {
      return false;
    }
  }
  return true;
}
int main(int argc, char const *argv[]) {
  int c, davg, n, p = 0;
  cin >> c >> d >> davg >> n;
  ability = c * davg;
  getchar();
  for (int i = 0; i < n; ++i) {
    oil temp;
    scanf("%lf %d", &temp.price, &temp.dis);
    o.push_back(temp);
  }
  sort(o.begin(), o.end(), cmpoilstart);
  if (o[0].dis) {
    cout << "The maximum travel distance = 0\n";
    return 0;
  }
  node first;
  first.start = 0, first.end = ability, first.price = o[0].price;
  v.push_back(first);
  m.push_back(first);
  int i = 0;
  while (!o[i].dis) {
    o.erase(o.begin() + i);
  }
  sort(o.begin(), o.end(), cmpoil);
  while (p != o.size() && !canreach()) {
    node temp;
    temp.start = o[p].dis;
    temp.price = o[p].price;
    int tempend = temp.start + ability;
    temp.end = (tempend > d) ? (d) : tempend;
    ++p;
    //		cout<<temp.start<<" "<<temp.end<<" "<<temp.price<<"
    //"<<canreach()<<"
    //"<<p<<" "<<v.size()<<" "<<m.size()<<endl;
    if (havein(temp)) {
      v.push_back(temp);
      margin(temp);
      //		for(int i=0;i<m.size();++i){
      //			cout<<'m'<<m[i].start<<" "<<m[i].end<<endl;
      //		}
      //		for(int i=0;i<v.size();++i){
      //			cout<<'v'<<v[i].start<<" "<<v[i].end<<"
      //"<<v[i].price<<endl;
      //		}
    } else if (lowprice(temp)) {
      v.push_back(temp);
    }
  }

  if (p == o.size() && !canreach()) {
    cout << "The maximum travel distance = " << m[0].end << endl;
  } else {
    int more = 0, tempstart;
    double spend = 0.0;
    sort(v.begin(), v.end(), cmpdis);
    for (int i = 1; i < v.size(); ++i) {
      tempstart = v[i].start - v[i - 1].start;
      if (v[i].price <= v[i - 1].price) {
        if (more < tempstart) {
          spend += (tempstart - more) * v[i - 1].price * 1.0;
          more = 0;
        } else {
          more -= tempstart;
        }

      } else {
        if (more >= 600) {
          more -= 600;
        } else {
          spend += (600 - more) * v[i - 1].price * 1.0;
          more = 600 - tempstart;
        }
      }
      //			cout<<v[i].start<<" "<<v[i-1].start<<"
      //"<<spend<<endl;
    }

    spend += (d - v[v.size() - 1].start - more) * 1.0 * v[v.size() - 1].price;
    printf("%.2f\n", spend / davg);
  }

  return 0;
}
