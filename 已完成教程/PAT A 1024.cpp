#include<iostream>
#include<string>
#include<vector>
using namespace std;
vector<int> v,any;
bool pal(vector<int> t){
	for(int i=0;i<t.size();++i){
		if(t[i]!=t[t.size()-1-i])
		return false;
	}
	return true;
}
void sum(){
	v=any;
	int x=0;
	for(int i=0;i<v.size();++i){
		int temp=v[i]+v[v.size()-1-i]+x;
			any[i]=temp%10;
			x=temp/10;
	}
	if(x!=0) any.push_back(x);
	return ;
}
void string2vector(string str){
	vector<int> q;
	bool vis=false;
	for(int i=0;i<str.size();++i){
		int temp=str[i]-'0';
		if(temp) vis=true;
		if(vis==false&&i!=str.size()-1){
		}
		else{
			q.push_back(temp);
		}
	}
	for(int i=q.size()-1;i>=0;--i){
		v.push_back(q[i]);
	}
	return ;
}

int main(){
	string str;
	int m;
	cin>>str>>m;
	string2vector(str);
	any=v;
	bool vis=false;
	for(int i=0;i<m;++i){
		if(pal(any)==true) {
			for(int j=0;j<any.size();++j){
				cout<<any[j];
			}
			cout<<endl<<i<<endl;
			vis=true;
			break;
		}
		sum();
	}
	if(vis==false){
		for(int j=any.size()-1;j>=0;--j){
			cout<<any[j];
		}
		cout<<endl<<m<<endl;
	}
	return 0;
	
	
	
}
