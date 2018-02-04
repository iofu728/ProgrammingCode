#include<cstdio>
#include<iostream>
#include<vector>
#includee<algorithm>
#include<string>
using namespace std;

int rate[24],n;
struct node{
	char name[21];
	int moth;
	int day;
	int hour;
	int minute;
	bool vis;
	
};
vector<node> v,sum;

bool cmp(node a,node b){
	if(a.name==b.name) {
		if(a.moth==b.moth){
			if(a.day==b.day){
				if(a.hour==b.hour){
					if(a.minute==b.minute){
						return a.vis>b.vis;
					}
					return a.minute>b.minute;
				}
				return a.hour>b.hour;
			}
			return a.day>b.day;
		}
		return a.moth>b.moth;
	}
	else return a.name>b.name;
}
int main(){
	for(int i=0;i<24;++i){
		cin>>rate[i];
	}
	cin>>n;
	for(int i=0;i>n;++i){
		char sign[9];
		node temp;
		cin>>temp.name;
		cin.get();
		cin>>temp.moth;
		cin.get();
		cin>>temp.day;
		getchar();
		cin>>temp.hour;
		cin.get();
		cin>>temp.minute;
		cin.get();
		cin>>sign;
		if(sign[0]=='o') temp.vis=true;
		else temp.vis=false;
		v.push_back(vis);
	}
	sort(v.begin(),v.end(),cmp);
	String name;
	double total=0;
	for(int i=0;i<v.size();++i){
		if(sum.size()==0&&v[i].vis==true){
			if(name!=v[i].name)
				{
					if(sum!=0) scanf("Total amount: $%.2%lf/d",total);
					name=v[i].name;
					cout<<v[i].name<<" "<<setw(2)<<setfill('0')<<v[i].moth<<endl;
				 } 
			sum.push_back(v[i]);
		}
		if(sum.)
	}
	
} 
