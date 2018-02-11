#include<cstdio>
#include<queue>
#include<vector>
using namespace std;

const int maxn=100;
vector<int> G[maxn];
int h[maxn]={0};
int max_h=0;
int leaf[maxn]={0};



void BFS(){
	queue<int> Q;
	Q.push(1);
	while(!Q.empty()){
		int front=Q.front();
		Q.pop();
		max_h=max(max_h,h[front]);
		if(G[front].size()==0)
		leaf[h[front]]++;
		for(int i=0;i<G[front].size();i++){
			h[G[front][i]]=h[front]+1;
			Q.push(G[front][i]);
		}
		
	}
	
}
int main(){
	int n,m;
	scanf("%d%d",&n,&m);
	
	for(int i=0;i<m;i++){
		int parent,child,k;
		scanf("%d%d",&parent,&k);
		for(int j=0;j<k;j++){
			scanf("%d",&child);
			G[parent].push_back(child);
		}
	
	}
	h[1]=1;
	BFS();
	for(int i=1;i<=max_h;i++){
		if(i==1)printf("%d",leaf[i]);
		else printf(" %d",leaf[i]);
		
	}
	return 0;
	
} 
