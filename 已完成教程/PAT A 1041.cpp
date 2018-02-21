#include<iostream>
#include<algorithm>
using namespace std;
const int maxn=100001;
int vis[maxn];
int u=0;
int main(){
	fill(vis,vis+maxn,0);
	int n;
	cin>>n;
	int v[n];
	for(int i=0;i<n;++i){
		cin>>v[i];
		++vis[v[i]];
	}
	for(int i=0;i<n;++i){
		int temp=v[u];
		if(vis[temp]==1){
			cout<<temp;
			return 0;
		}else{
			++u;
		}
	}
	cout<<"None";
	return 0;
	
}
