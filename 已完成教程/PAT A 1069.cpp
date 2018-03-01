#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;
bool cmp(int a,int b){
	return a>b;
}
int main(){
	string str;
	cin>>str;
	int temp=0,sv=0,cx=0;
	str.insert(0,4-str.size(),'0');//补充前置0  
	vector<int> vs;
	for(int i=0;i<4;++i){
		vs.push_back(str[i]-'0');
	}

	for(int i=0;i<4;++i){
		cx=cx*10+vs[i];
	}
	sort(vs.begin(), vs.end(),cmp);
	for(int i=0;i<4;++i){
		temp=temp*10+vs[i];
	}

	do{
		sv=0;
		for(int i=3;i>=0;--i){
			sv=sv*10+vs[i];
		}
		printf("%04d - %04d = %04d\n",temp,sv,temp-sv);
		vs.clear();
		cx=temp-sv;
		while(cx>9){
			vs.push_back(cx%10);
			cx/=10;
		}
		vs.push_back(cx);
		cx=temp-sv;
		while(vs.size()<4){
			vs.push_back(0);
		}
		sort(vs.begin(), vs.end(),cmp);
		temp=0;
		for(int i=0;i<4;++i){
			temp=temp*10+vs[i];
		}
	}while(cx!=6174&&cx!=0); 
	
	return 0;
}
