#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;
vector<int> in,level;
void leverorder(int start,int end, int index){
	if(start>end){
		return ;
	}else{
		int n=end-start+1;
		int l=log(n+1)/log(2);
		int lever=n-(pow(2,l)-1);
		int temp=pow(2,l-1); 
		int root=start+temp-1+min(temp,lever);
		level[index]=in[root];
		leverorder(start,root-1,2*index+1);
		leverorder(root+1,end,2*index+2);
	}
}
int main(){
	int n;
	scanf("%d",&n);
	in.resize(n);
	level.resize(n);
	for(int i=0;i<n;++i){
		scanf("%d",&in[i]);
	}
	sort(in.begin(), in.end());
	leverorder(0,n-1,0);
	for(int i=0;i<n-1;++i){
		cout<<level[i]<<" ";
	}
	cout<<level[n-1];
	return 0;
}
