#include<iostream>
using namespace std;
int len=0,changes[30];
bool change(int n,int m){
	do{
		changes[len++]=n%m;
		n/=m;
	}while(n);
	for(int i=0;i<=len/2;++i){
		if(changes[i]!=changes[len-i-1])
			return false;
	}
	return true;
}
int main(){
	int n,m;
	cin>>n>>m;
	bool vis=change(n,m);
	if(vis==false) cout<<"No\n";
	else cout<<"Yes\n";

	for(int i=len-1;i>0;--i){
		cout<<changes[i]<<" ";
	}
	cout<<changes[0]<<endl;
	return 0;
} 
