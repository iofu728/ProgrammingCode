#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;

bool cmp(string a,string b){
	return a+b<b+a;
}
int main(){
	int n;
	cin>>n;
	vector<string> v(n);
	for(int i=0;i<n;++i){
		cin>>v[i];
	}
	sort(v.begin(), v.end(),cmp);
	string sum;
	for(int i=0;i<n;++i){
		sum+=v[i];
	}
	while(sum.size()!=0&&sum[0]=='0')
		sum.erase(sum.begin());
	if(!sum.size())
		cout<<'0'<<endl;
	else{
		cout<<sum<<endl; 
	}
	return 0;
}
