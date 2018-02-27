#include<iostream>
using namespace std;
int main(){
	int n;
	long long a,b,c;
	cin>>n;
	getchar();
	for(int i=0;i<n;++i){
		cin>>a>>b>>c;
		getchar();
		long long sum=a+b;
		cout<<"Case #"<<i+1;
		if(a>0&&b>0&&sum<0){
			cout<<": true\n";
		}else if(a<0&&b<0&&sum>=0){
			cout<<": false\n";
		}else if(sum>c){
			cout<<": true\n";
		}else{
			cout<<": false\n";
		}
	} 
	return 0;
}
