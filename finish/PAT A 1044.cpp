#include <iostream>
#include <vector>
using namespace std;
const int INF = 0x3fffffff;
int n, m;
struct node {
  int sum, p, q;
};

int main(int argc, char const *argv[]) {
  int maxmin = INF, p = 0, q = 0, sum = 0, temp = 0;
  bool vis = false;
  vector<node> v;
  cin >> n >> m;
  int dis[n + 1];
  getchar();
  for (int i = 1; i <= n; ++i) {
    cin >> temp;
    sum += temp;
    dis[i] = sum;
  }
  getchar();
  sum = 0;
  dis[0] = 0;
  while (p <= n && q <= n && p <= q) {
    if (sum == m) {
      cout << p + 1 << "-" << q << endl;
      vis = true;
      ++q;
      if (q <= n) {
        sum = dis[q] - dis[p];
      }
    } else if (sum < m) {
      //			cout<<"*"<<sum<<" "<<p<<" "<<q<<endl;
      ++q;
      if (q <= n) {
        sum = dis[q] - dis[p];
      }
    } else {
      if (sum <= maxmin) {
        //				cout<<"--";
        if (sum < maxmin) {
          v.clear();
        }
        node temp;
        temp.p = p, temp.q = q, maxmin = sum, temp.sum = sum;
        v.push_back(temp);
      }
      if (p == q - 1) {
        //				cout<<"??";
        ++p;
        ++q;
      } else {
        //				cout<<"<>";
        ++p;
      }
      sum = dis[q] - dis[p];
    }
  }
  if (!vis) {
    for (int i = 0; i < v.size(); ++i) {
      cout << v[i].p + 1 << "-" << v[i].q << endl;
    }
  }
  return 0;
}
//#include <iostream>
//#include <vector>
// using namespace std;
// vector<int> sum, resultArr;
// int n, m;
// void Func(int i, int &j, int &tempsum) {
//    int left = i, right = n;
//    while(left < right) {
//        int mid = (left + right) / 2;
//        if(sum[mid] - sum[i-1] >= m)
//            right = mid;
//        else
//            left = mid + 1;
//    }
//    j = right;
//    tempsum = sum[j] - sum[i-1];
//}
// int main() {
//    scanf("%d%d", &n, &m);
//    sum.resize(n+1);
//    for(int i = 1; i <= n; i++) {
//        scanf("%d", &sum[i]);
//        sum[i] += sum[i-1];
//    }
//    int minans = sum[n];
//    for(int i = 1; i <= n; i++) {
//        int j, tempsum;
//        Func(i, j, tempsum);
//        if(tempsum > minans) continue;
//        if(tempsum >= m) {
//            if(tempsum < minans) {
//                resultArr.clear();
//                minans = tempsum;
//            }
//            resultArr.push_back(i);
//            resultArr.push_back(j);
//        }
//    }
//    for(int i = 0; i < resultArr.size(); i += 2)
//        printf("%d-%d\n", resultArr[i], resultArr[i+1]);
//    return 0;
//}
