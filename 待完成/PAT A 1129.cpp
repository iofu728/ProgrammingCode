#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;
const int INF=0x3fffffff;

struct node{
	int rec,count,indices;
};
vector<node> v;
bool cmp(node mm,node nn){
	if(mm.count==nn.count) return mm.rec<nn.rec;
	else return mm.count>nn.count;
}
int find_num(int num){
	int n;
	if(v.size()<500) n=v.size();
	else n=500;
	
	for(int i=0;i<n;++i){
		if(v[i].rec==num){
			return i;
		}
	}
	return INF;
}
int main(){
	int n,k,t=0;
	cin>>n>>k;
	node temp;
	cin>>temp.rec;
	temp.count=1;
	temp.indices=t;
	++t;
	v.push_back(temp);
	int xtemp;
	for(int i=1;i<n;++i){
		cin>>xtemp;
		cout<<xtemp<<":";
		int xxx=v.size();
		for(int j=0;j<min(k,xxx);++j){
			cout<<" "<<v[j].rec;
		}
		/*for(int j=0;j<v.size();++j){
			cout<<" "<<v[j].count;
		} 
		cout<<" "<<find_num(xtemp);*/
		cout<<endl;
		int xI=find_num(xtemp);
		if(xI!=INF){
			++v[xI].count;
		}
		else{
				temp.count=1;
				temp.rec=xtemp;
				temp.indices=t;
				++t;
				v.push_back(temp);
				xI=v.size()-1;
		}
		if(v.size()<50){
			sort(v.begin(),v.end(),cmp);
		}
		else sort(v.begin(),v.begin()+49,cmp);
		if(xI>k){
		swap(v[k+1],v[xI]);
		}
	}
	return 0;
}
