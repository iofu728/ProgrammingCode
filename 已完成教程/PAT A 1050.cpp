#include<iostream>
#include<cstring>
#include<map>
using namespace std;
const int maxn=10001;
char wait[maxn],metch[maxn];
map<char,int > mmp;
int main(){
	char temp;
	cin.getline(wait,maxn);
	cin.getline(metch,maxn);
	int len1=strlen(wait),len2=strlen(metch);
	for(int i=0;i<len2;++i){
		mmp[metch[i]]=1;
	}
	for(int i=0;i<len1;++i){
		if(mmp.find(wait[i])==mmp.end()) cout<<wait[i];
	}
	return 0;
}
