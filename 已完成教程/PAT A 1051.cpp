#include<iostream>
#include<stack>
#include<vector>
using namespace std;
int main(int argc, char const *argv[])
{
	int n,m,k;
	cin>>m>>n>>k;
	getchar();
	for(int i=0;i<k;++i){
		bool vis=false;
		stack<int> s;
		vector<int> v(n+1);
		for(int j=1;j<=n;++j){
			scanf("%d",&v[j]);
		}
		int current=1;
		for(int j=1;j<=n;++j){
			s.push(j);
			if(s.size()>m) break;
			while(!s.empty()&&s.top()==v[current]){
				s.pop();
				current++;
			}
		}
		if(current==n+1){
			vis=true;
		}
		if(vis){
			printf("YES\n");
		}else{
			printf("NO\n");
		}
	}
	return 0;
}
