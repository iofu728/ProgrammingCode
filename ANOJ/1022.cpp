#include<iostream>
#include<string>
#include<map>
#include<algorithm>
using namespace std;

int main(){

	int n;
	cin>>n;
	getchar();
	int num=0;
	for(int i=0;i<n;++i){
		string str;
		cin>>str;
		map<char,int> a;
		for(int j=0;j<str.size();++j){
			if(isalpha(str[j])){
				char b=str[j];
				a[b]=1;
			}
		}
		num+=a.size();
	}
	cout<<num<<endl;
	return 0;
}
