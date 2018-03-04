#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;
const int INF=0x3fffffff;
const int maxn=1020;
int n,m,k,dg,maxd,mind;
double avag;
int G[maxn][maxn],d[maxn];
bool vis[maxn];

struct node
{
	int mindis;
	double id,avagd;
	bool canServer;
	
};
vector<node> v; 
bool cmp(node a,node b){
	return (a.canServer==b.canServer)?((a.mindis==b.mindis)?(a.id<b.id):(a.mindis>b.mindis)):(a.canServer>b.canServer);
}
void Dijkstra(int start){
	fill(d,d+maxn,INF);
	fill(vis,vis+maxn,false);
	d[start]=0;
	for(int i=1;i<=n+m;++i){
		int u=-1,MIN=INF;
		for(int j=1;j<=n+m;++j){
			if(!vis[j]&&d[j]<MIN){
				u=j;
				MIN=d[j];
			}
		}
		if(u==-1) return ;
		vis[u]=true;
		for(int v=1;v<=n+m;++v){
			if(!vis[v]&&G[u][v]!=INF&&d[u]+G[u][v]<d[v]){
				d[v]=d[u]+G[u][v];
			}
		}
	}
	return ;
}
void findm(int start){
	double sum=0,num=0;
	mind=INF,maxd=-1;	
	for(int i=1;i<=n;++i){
		if(d[i]<mind&&i!=start){
			mind=d[i];
		}
		if(d[i]!=INF&&d[i]>maxd&&i!=start){
			maxd=d[i];
		}
		if(d[i]!=INF){
			sum+=d[i];
			++num;
		}
//		cout<<d[i]<<' ';
	}
//	cout<<sum<<' '<<num<<endl;
	avag=sum/num*1.0;
	return ;
}
int stringnum(string str){
	if(str[0]=='G'){
		return (str[1]-'0')+n;
	}
	else return str[0]-'0';
}
int main(){
	cin>>n>>m>>k>>dg;
	getchar();
	fill(G[0],G[0]+maxn*maxn,INF);
	for(int i=0;i<k;++i){
		int id1,id2;
		string str1,str2;
		cin>>str1>>str2;
		id1=stringnum(str1);
		id2=stringnum(str2);
		cin>>G[id1][id2];
		G[id2][id1]=G[id1][id2];
		getchar();
	}
	for(int i=n+1;i<=n+m;++i){
		node temp;
		Dijkstra(i);
		findm(i);
		temp.mindis=mind;
		if(maxd>dg){
			temp.canServer=false;
		}else{
			temp.canServer=true;
		}
		temp.id=i-n+1;
		temp.avagd=avag;
		v.push_back(temp);
//		cout<<temp.id<<' '<<temp.mindis<<' '<<temp.avagd<<' '<<temp.canServer<<' '<<maxd<<' '<<mind<<endl;
	}
	sort(v.begin(), v.end(),cmp);
	if(v[0].canServer==false){
		cout<<"No Solution\n";
	}else{
		cout<<'G'<<v[0].id<<endl;
		printf("%.1d.0 %.1f\n", v[0].mindis,round(v[0].avagd*10)/10.0);
	}
	return 0;
}
