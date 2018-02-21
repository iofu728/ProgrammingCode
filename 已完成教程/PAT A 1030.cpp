#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

const int maxn=501;
const int INF=0x3fffffff;

bool vis[maxn]={false};
int G[maxn][maxn],cost[maxn][maxn];
int n,m,s,d,dis[maxn],mincost=INF;
vector<int> pre[maxn],temppath,path;

void Dijkstra(int s){
	fill(dis,dis+maxn,INF);
	fill(vis,vis+maxn,false);
	dis[s]=0;
	for(int i=0;i<n;++i){
		int u=-1,MIN=INF;
		for(int j=0;j<n;++j){
			if(!vis[j]&&dis[j]<MIN){
				u=j;
				MIN=dis[j];
			}
		}
		if(u==-1) return;
		vis[u]=true;
		for(int v=0;v<n;++v){
			if(G[u][v]!=INF&&!vis[v]){
				if(dis[u]+G[u][v]<dis[v]){
					dis[v]=dis[u]+G[u][v];
					pre[v].clear();
					pre[v].push_back(u);
				}else if(dis[u]+G[u][v]==dis[v]){
					pre[v].push_back(u);
				}
			}
		}
	}

}

void DFS(int v){
	if(v==s){
		temppath.push_back(v);
		int tempcost=0;
		for(int i=temppath.size()-1;i>0;--i){
			int id=temppath[i],idnext=temppath[i-1];
			tempcost+=cost[id][idnext];
		}
		if(tempcost<mincost){
			mincost=tempcost;
			path=temppath;
		}
		temppath.pop_back();
		return ;
	}
	temppath.push_back(v);
	for(int i=0;i<
	pre[v].size();++i){
		DFS(pre[v][i]);
	}
	temppath.pop_back();
}
int main(){
	fill(G[0],G[0]+maxn*maxn,INF);
	fill(cost[0],cost[0]+maxn*maxn,INF);
	cin>>n>>m>>s>>d;
	getchar();
	for(int i=0;i<m;++i){
		int start,end;
		cin>>start>>end;
		cin>>G[start][end]>>cost[start][end];
		getchar();
		G[end][start]=G[start][end];
		cost[end][start]=cost[start][end];
	}
	Dijkstra(s);
	DFS(d);
	for(int i=path.size()-1;i>=0;--i){
		cout<<path[i]<<" ";
	}
	cout<<dis[d]<<" "<<mincost<<endl;
	return 0;
}
