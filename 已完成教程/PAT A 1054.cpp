#include<iostream>
#include<map>
using namespace std;
map<int,int> mmp;

int main(){
	int n,m,temp;
	scanf("%d %d",&n,&m);
	int G[n][m];
	for(int i=0;i<m;++i){
		for(int j=0;j<n;++j){
			scanf("%d",&temp);
			if(mmp.find(temp)==mmp.end()){
				mmp[temp]=0;
			}else{
				++mmp[temp];
			}
		}
	}
	int mid=n*m/2,most=-1;
	for(auto it:mmp){
		if(it.second>=mid){
			most=it.first;
		}
	}
	if(most==-1){
		printf("No\n");
	}else{
		printf("%d\n",most);
	}
	return 0;
}
