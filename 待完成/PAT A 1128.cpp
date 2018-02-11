#include<cstring>
#include<algorithm>
#include<cstring>
#include<iostream>
#include<cmath>
using namespace std;

int main() {
	int num;
	cin >> num;
	for (int i = 0; i < num; ++i) {
		bool vis = true;
		int m;
		cin >> m;
		int P[m];
		for (int j = 0; j < m; ++j) {
			cin >> P[j];
		}
		for (int j = 0; j < m-1; ++j) {
			for (int k = j + 1; k < m; ++k) {
				if(abs(j - k) == abs(P[j] - P[k])||P[j]==P[k]) {
					vis = false;
					goto mmp;
				}
			}
		}
	mmp:
		if (vis == false) printf("NO\n");
		else printf("YES\n");
	}
	return 0;
}


