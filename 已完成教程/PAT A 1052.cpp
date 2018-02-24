#include<iostream>
#include<vector>
#include<map>
#include<algorithm>
using namespace std;

struct node
{
	int id,next,data;
};
bool cmp(node a,node b){
	return a.data<b.data;
}
map<int,node> mmp;
int main(){
	int n,start,front;
	cin>>n>>start;
	getchar();
	vector<node> v;
	for(int i=0;i<n;++i){
		node temp;
		cin>>temp.id>>temp.data>>temp.next;
		mmp[temp.id]=temp;
		getchar();
	}
	int now=start;
	while(now!=-1){
		node temp=mmp[now];
		v.push_back(temp);
		now=temp.next;
	}
	sort(v.begin(), v.end(),cmp);
	if(v.size()){
		printf("%d %05d\n",v.size(),v[0].id);
		for(int i=0;i<v.size()-1;++i){
			printf("%05d %d %05d\n",v[i].id,v[i].data,v[i+1].id);
		}
		printf("%05d %d -1\n",v[v.size()-1].id,v[v.size()-1].data);
	}else{
		cout<<"0 -1\n";
	}

	return 0;
}
