#include <iostream>
#include<string>
using namespace std;

const int maxn=1002;
int dp[maxn][maxn];

int main(){
	string str;
	getline(cin,str);
	int size=str.size(),len=1;
	for(int i=0;i<size;++i){
		dp[i][i]=1;
		if(i<size-1&&str[i]==str[i+1]){
			dp[i][i+1]=1;
			len=2;
		}
	}
	for(int L=3;L<=size;++L){
		for(int i=0;i+L-1<size;++i){
			int j=i+L-1;
			if(str[i]==str[j]&&dp[i+1][j-1]==1){
				dp[i][j]=1;
				len=L;
			}
		}
	}
	cout<<len<<endl;
	return 0;
}
