#include<iostream>
#include<vector>
using namespace std;
int main(){
	int n,num,cnt=0,index=1,ans=0;
	scanf("%d",&n);
	vector<int> v(n);
	for(int i=0;i<n;++i){
		scanf("%d",&num);
		v[num]=i;
		if(num!=i&&num!=0){
			++cnt;
		}
	}
	while(cnt>0){
		if(v[0]==0){
			while(index<n){
				if(v[index]!=index){
					swap(v[index],v[0]);
					++ans;
					break;
				}
				++index;
			}
		}
		while(v[0]){
			swap(v[v[0]],v[0]);
			++ans;
			--cnt;
		}
	}
	printf("%d",ans);
	return 0;
}