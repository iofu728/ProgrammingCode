#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

struct node {
  int id, sum = 0, grade[5] = {-1, -1, -1, -1, -1}, perferNum = 0;
  bool havePush = false;
};

bool compareNode(node a, node b) {
  return a.sum == b.sum
             ? (a.perferNum == b.perferNum ? a.id < b.id
                                           : a.perferNum > b.perferNum)
             : a.sum > b.sum;
}

int main(int argc, char const *argv[]) {
  int n, k, m, uid, cid, tempGrade, rank = 1;
  cin >> n >> k >> m;
  std::vector<node> userList(n);
  int totalGrade[k];
  for (int i = 0; i < k; ++i) cin >> totalGrade[i];
  for (int i = 0; i < m; ++i) {
    cin >> uid >> cid >> tempGrade;
    if (tempGrade == -1) {
      userList[uid - 1].id = uid;
      userList[uid - 1].grade[cid - 1] = 0;
    }
    if (userList[uid - 1].grade[cid - 1] < tempGrade) {
      userList[uid - 1].id = uid;
      if (userList[uid - 1].grade[cid - 1] != -1)
        userList[uid - 1].sum -= userList[uid - 1].grade[cid - 1];
      userList[uid - 1].sum += tempGrade;
      userList[uid - 1].grade[cid - 1] = tempGrade;
      if (tempGrade == totalGrade[cid - 1]) ++userList[uid - 1].perferNum;
      userList[uid - 1].havePush = true;
    }
  }
  sort(userList.begin(), userList.end(), compareNode);

  for (int i = 0; i < n; ++i) {
    if (userList[i].havePush) {
      if (i && userList[i].sum == userList[i - 1].sum) {
        cout << rank << ' ';
      } else {
        cout << i + 1 << ' ';
        rank = i + 1;
      }
      printf("%05d %d", userList[i].id, userList[i].sum);
      for (int j = 0; j < k; ++j) {
        if (userList[i].grade[j] == -1) {
          cout << " -";
        } else {
          cout << ' ' << userList[i].grade[j];
        }
      }
      if (i != n - 1) cout << endl;
    }
  }
  return 0;
}
