#include<cstdio>
#include<vector>
#include<cstring>
#include<algorithm>
using namespace std;

const int maxn=510;
const int INF=0x3fffffff;

int n,m,st,ed,G[maxn][maxn],cost[maxn][maxn];
int d[maxn],mincost=INF;
bool vis[maxn]={false};
vector<int> pre[maxn];
vector<int> temppath,path;

void Dijkstra(int s){
	fill(d,d+maxn,INF);
	d[s]=0;
	for(int i=0;i<n;i++){
		int u=-1,MIN=INF;
		for(int j=0;j<n;j++){
			if(vis[j]==false&&d[j]<MIN){
				u=j;
				MIN=d[j];
			}
		}
		if(u==-1)return;
		vis[u]=true;
		for(int v=0;v<n;v++){
			if(vis[v]==false&&G[u][v]!=INF){
				if(d[u]+G[u][v]<d[v]){
					d[v]=d[u]+G[u][v];
					pre[v].clear();
					pre[v].push_back(u);
					 
				}
				else if(d[u]+G[u][v]==d[v]){
					pre[v].push_back(u);
				}
			}
		}
	}
}

void DFS(int v){
	if(v==st){
		temppath.push_back(v);
		int tempcost=0;
		for(int i=temppath.size()-1;i>0;i--){
			int id=temppath[i],idnext=temppath[i-1];
			tempcost+=cost[id][idnext];
		}
		if(tempcost<mincost){
			mincost=tempcost;
			path=temppath;
		}
		temppath.pop_back();
		return;
	}
	temppath.push_back(v);
	for(int i=0;i<pre[v].size();i++){
		DFS(pre[v][i]);
	}
	temppath.pop_back();
}

int main(){
	scanf("%d%d%d%d",&n,&m,&st,&ed);
	int u,v;
	fill(G[0],G[0]+maxn*maxn,INF);
	fill(cost[0],cost[0]+maxn*maxn,INF);
	for(int i=0;i<m;i++){
		scanf("%d%d",&u,&v);
		scanf("%d%d",&G[u][v],&cost[u][v]);
		G[v][u]=G[u][v];
		cost[v][u]=cost[u][v];
	}
	Dijkstra(st);
	DFS(ed);
	for(int i=path.size()-1;i>=0;i--){
		printf("%d ",path[i]); 
	}
	printf("%d %d ",d[ed],mincost);
	return 0;
}
