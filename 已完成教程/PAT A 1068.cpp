#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
const int maxn=10010;
const int maxs=110;
bool cmp(int a,int b){
	return a>b;
}
int main(){
	int n,m,dp[maxs],w[maxn],choice[maxn][maxs];//dp表示，w表示物品重量，choice表示第i个coin选择后总价值为j，存放的值为是否选择。
	fill(choice[0],choice[0]+maxs*maxn,0);
	fill(dp,dp+maxs,0);
	scanf("%d%d",&n,&m);
	for(int i=0;i<n;++i){
		scanf("%d",&w[i]);
	}
	sort(w,w+n,cmp);
	for(int i=0;i<n;++i){
		for(int j=m;j>=w[i];--j){
			if(dp[j-w[i]]+w[i]>=dp[j]){
				dp[j]=dp[j-w[i]]+w[i];
				choice[i][j]=1;
			}
		}
	}
    int MAX=-1,ans=-1;
    for(int v=0;v<=m;v++){
        if(dp[v]>MAX){
            MAX=dp[v];
            ans=v;
        }
    }
    if(ans!=m){
        printf("No Solution\n");
        return 0;
    }
    bool flag[maxn]={0};
    for(int i=n-1;i>=0;i--){
        if(choice[i][ans]==1){
            flag[i]=true;
            ans-=w[i];
        }
    }
    int tag=1;
    for(int i=n-1;i>=0;i--){
        if(flag[i]==true){
            if(tag) tag=0;
            else printf(" ");
            printf("%d",w[i]);            
        }
    }

	return 0;
}
