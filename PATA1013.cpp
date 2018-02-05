#include<cstdio>

const int maxn=1010;
int G[maxn][maxn];
bool test[maxn][maxn]={false};
int n,m,k;
bool memeoy;
int search(int x){
	fill(test,test+maxn*maxn,flase);
	memeoy=true;
	int start=0;
	if(x==1){
		start=2;
	}
	for(int i=star;i<n&&i!=x;i++){
		for(int j=i+1;j<n&&j!=x&&j!=i;j++){
			if(G[i][j]==1){
				test[i][j]=true;
			}
			for(int k=1;k<i;i++){
				if(test[k][i]==true){
					test[k][j]=true;
				}
			}
		}
	}
	for()
	for(int i=star;i<n&&i!=x;i++){
		for(int j=i+1;j<n&&j!=x;j++){
			if(test[i][j]==false){
				memeoy=false;
			}
		}
	}
	if(memeory==true) return 0;
	else return 
	
	
}
int main(){
	fill(G,G+maxn*maxn,0);
	scanf("%d %d %d",&n,&m,&k);
	int u,v;
	int goal[k];
	for(int i=0;i<m;i++){
		scanf("%d %d",&u,&v);
		G[u][v]=1;
		G[v][u]=1;
	}
	for(int i=0;i<k;i++){
		scanf("%d",&goal[i]);
	}
	
	
} 
