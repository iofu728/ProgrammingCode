#include <iostream>
#include<vector>
#include<queue>
#include<algorithm>
#include<cmath>
using namespace std;
const int maxn=101;

struct node
{	
	int come,spend,start,wait;
	bool vip;
};

struct tablenode
{
	int poptime=0,num,time=0;
	bool vip=false;
};

node tempvip;
vector<node> v,q;
bool vis[maxn]={false};
int vipid,mm,hh,ss;

bool cmp(node a,node b){
	return a.come<b.come;
}
bool cmpvip(node a,node b){
	return ((a.vip==b.vip)?(a.come<b.come):(a.vip>b.vip));
}
bool cmptable(tablenode a,tablenode b){
	return ((a.poptime==b.poptime)?(a.num<b.num):(a.poptime<b.poptime));
}
bool cmptables(tablenode a,tablenode b){
	return a.num<b.num;
}
bool findvip(){
	for(int i=0;i<q.size();++i){
		if(q[i].vip){
			tempvip=q[i];
			vipid=i;
			return true;
		}
	}
	return false;
}
void changetime(int time){
	hh=time/3600+8;
	time%=3600;
	mm=time/60;
	ss=time%60;
	return ;
}

int main(int argc, char const *argv[])
{
	int n,k,m,sp,vi,cometime;
	cin>>n;
	getchar();
	for (int i = 0; i < n; ++i)
	{
		node temp;
		scanf("%d:%d:%d %d %d",&hh,&mm,&ss,&sp,&vi);
		cometime=(hh-8)*3600+(mm)*60+ss;
		temp.come=cometime;
		temp.spend=((sp>=120)?120:sp);
		temp.vip=((vi)?true:false);
		if(cometime<=46800){
			q.push_back(temp);
		}
	}
	scanf("%d %d",&k,&m);
	std::vector<tablenode> table(k);
	for (int i = 0; i < m; ++i)
	{
		int temp;
		scanf("%d",&temp);
		table[temp-1].vip=true;	
		table[temp-1].num=temp;
	}
	for (int i = 0; i < k; ++i)
	{
		if(!table[i].vip) table[i].num=i+1;
	}
	sort(q.begin(), q.end(),cmp);
//	for(int i=0;i<table.size();++i){
//		cout<<table[i].poptime<<" "<<table[i].num<<" "<<table[i].time<<" "<<table[i].vip<<endl;
//	}
	for (int i = 0; i < n; ++i)
	{
		sort(table.begin(), table.end(),cmptable);
//		cout<<table[0].num<<endl;
		node temp=q[0];
		if(table[0].vip==false||(!findvip())){
			q.erase(q.begin());	
			if(table[0].poptime<=temp.come){
				temp.start=temp.come;
				table[0].poptime=temp.come+temp.spend*60;
				temp.wait=0;
//				cout<<"*"<<temp.come<<" "<<temp.start<<" "<<temp.spend<<" "<<temp.wait<<" "<<table[0].poptime<<endl; 
			}else{
				temp.start=table[0].poptime;
				table[0].poptime+=temp.spend*60;
				temp.wait=temp.start-temp.come;
//				cout<<"**"<<temp.come<<" "<<temp.start<<" "<<temp.spend<<" "<<temp.wait<<" "<<table[0].poptime<<endl; 
			}
			if(temp.start<46800){
				v.push_back(temp);
				++table[0].time;
			} 			
		}else{			
//	   		cout<<tempvip.come<<" "<<table[0].poptime<<" "<<tempvip.vip<<endl;
			if(table[0].poptime>=tempvip.come){
				q.erase(q.begin()+vipid);
				tempvip.start=table[0].poptime;
				table[0].poptime+=tempvip.spend*60;
				tempvip.wait=tempvip.start-tempvip.come;
//				cout<<"#"<<tempvip.come<<" "<<tempvip.start<<" "<<tempvip.spend<<" "<<tempvip.wait<<" "<<table[0].poptime<<endl; 
				if(tempvip.start<46800){
					++table[0].time;
					v.push_back(tempvip);
				}			
			}else{
				q.erase(q.begin());
				if(table[0].poptime<=temp.come){
					temp.start=temp.come;
					table[0].poptime=temp.come+temp.spend*60;
					temp.wait=0;
//					cout<<"##"<<temp.come<<" "<<temp.start<<" "<<temp.spend<<" "<<temp.wait<<" "<<table[0].poptime<<endl; 
				}else{
					temp.start=table[0].poptime;
					table[0].poptime+=temp.spend*60;
					temp.wait=temp.start-temp.come;
//					cout<<"###"<<temp.come<<" "<<temp.start<<" "<<temp.spend<<" "<<temp.wait<<" "<<table[0].poptime<<endl; 
				}
				if(temp.start<46800){
					++table[0].time;
					v.push_back(temp);
				}		
			}
		}
	}
	for (int i = 0; i < v.size(); ++i)
	{
		changetime(v[i].come);
		printf("%02d:%02d:%02d ",hh,mm,ss);
		changetime(v[i].start);
		printf("%02d:%02d:%02d %d\n",hh,mm,ss,int(round(v[i].wait/60.0)));
	}
	sort(table.begin(), table.end(),cmptables);
//	cout<<table.size()<<endl;
	for (int i = 0; i < table.size()-1; ++i)
	{
		printf("%d ",table[i].time);
	}
	printf("%d\n",table[table.size()-1].time);
	return 0;
}
