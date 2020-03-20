#include <algorithm>
#include <cstdio>
#include <iostream>
#include <stack>
#include <string>
#include <vector>
using namespace std;

string A[10] = {"zero", "one", "two",   "three", "four",
                "five", "six", "seven", "eight", "nine"};

int main() {
  string str;
  int temp, sum = 0;
  getline(cin, str);
  stack<int> s;
  for (int i = 0; i < str.size(); i++) {
    sum += str[i] - '0';
  }
  while (sum > 9) {
    temp = sum % 10;
    sum = sum / 10;
    s.push(temp);
  }
  s.push(sum);
  while (!s.empty()) {
    temp = s.top();
    s.pop();
    for (int j = 0; j < A[temp].size(); ++j) {
      cout << A[temp][j];
    }
    if (!s.empty()) {
      cout << " ";
    }
  }

  return 0;
}
