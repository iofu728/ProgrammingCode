#include<iostream>
#include<map>
#include<string>
#include<algorithm>
#include<cctype>
using namespace std;

int main(){
	string str,temp;
	getline(cin,str);
	map<string,int> mmp;
	for(int i=0;i<str.size();++i){
		if(isalnum(str[i])){
			str[i]=tolower(str[i]);
			temp+=str[i];
		}
		if(!isalnum(str[i])||i==str.size()-1){
			if(temp.size()){
				mmp[temp]++;
				temp.clear();
			}
		}
	}
	int max=-1;
	string maxstr;

	for(auto it:mmp){
		if(it.second>max){
			max=it.second;
			maxstr=it.first;
		}
	}
	cout<<maxstr<<' '<<max<<endl;
	return 0;

}
