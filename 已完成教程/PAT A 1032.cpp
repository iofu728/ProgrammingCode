#include<iostream>
#include<map>
#include<vector>
#include<algorithm>
using namespace std;

const int maxn=100001;
map<int,vector<int> > mmp;
struct node
{
	int next;
	char data;
}Node[maxn];

int main(){
	int s1,s2,n;
	cin>>s1>>s2>>n;
	getchar();
	for(int i=0;i<n;++i){
		int temp;
		cin>>temp;
		cin>>Node[temp].data>>Node[temp].next;
		getchar();
	}
	int now=s1;
	while(now!=-1){
		mmp[now].push_back(1);
		now=Node[now].next;
	}
	now=s2;
	while(now!=-1){
		if(mmp[now].size()){
			printf("%05d\n",now);
			return 0;
		}else{
			now=Node[now].next;
		}
	}
	cout<<"-1\n";
	return 0;

}
