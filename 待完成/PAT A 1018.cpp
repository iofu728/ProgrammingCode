#include<iostream> 
#include<vector>
#include<cmath>
using namespace std;

const int maxn=501;
const int INF=0x3fffffff;
int G[maxn][maxn],unin[maxn],d[maxn];
bool vis[maxn];
int c,n,s,m,spend=0,len=0,spendmin=INF,cost;
vector<int> lines,linebest;
vector<int> store[maxn];
void Dijkstra(){
	fill(vis,vis+maxn,false);
	fill(d,d+maxn,INF);
	d[0]=0;
	for(int i=0;i<n;++i){
		int u=-1,MIN=INF;
		for(int j=0;j<n;++j){
			if(vis[j]==false&&d[j]<MIN){
				u=j;
				MIN=d[j];
			}
		}
		if(u==-1) return ;
		vis[u]=true;
		for(int v=0;v<n;++v){
			if(vis[v]==false&&G[u][v]!=INF&&d[u]+G[u][v]<=d[v]){
				if(d[u]+G[u][v]<d[v]) store[v].clear();
				store[v].push_back(u);
				d[v]=d[u]+G[u][v];
			}
		}
	}
}
void DFS(int st){
	if(st==0){
		int cost=spend-len*c/2;
		if(abs(cost)<abs(spendmin)){
			spendmin=cost;
			linebest=lines;
		}
		return ;
	}
	vector<int> temp=store[st];
	for(int i=0;i<temp.size();++i){
		spend+=unin[temp[i]];
		++len;
		lines.push_back(temp[i]);
		DFS(temp[i]);
		spend-=unin[temp[i]];
		--len;
		lines.pop_back();
	}
	
}
int main(){
	cin>>c>>n>>s>>m;
	fill(G[0],G[0]+maxn*maxn,INF);
	for(int i=0;i<n;++i){
		cin>>unin[i];
	}
	int line,row;
	for(int i=0;i<m;++i){
		cin>>line>>row;
		scanf("%d",&G[line][row]); 
		G[row][line]=G[line][row];
	}
	Dijkstra();
	DFS(s);
	int out,in;
	if(spendmin<0){
		in=-spendmin,out=0;
	}
	else{
		out=spendmin,in=0;
	}
	cout<<out<<" ";
	for(int i=linebest.size();i>=0;--i){
		cout<<linebest[i]<<"->";
	}
	cout<<s<<" "<<in<<endl;
	return 0;
	
}

