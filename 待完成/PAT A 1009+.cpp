#include<cstdio>
const int N=1010;

int main(){
	int n,m,k,a,b,h,set=0;
	
	
	scanf("%d",&n);
	scanf("%d ",&k);
	double num[k+1]={0.0};
	scanf("%lf",&num[k]);	
	for(int i=1;i<n;i++){
		scanf("%d ",&a);
		scanf("%lf",&num[a]);
	}
	scanf("%d",&m);
	scanf("%d",&h);
	double nun[h+1]={0.0},sum[k+h+1]={0.0};
	bool vis[k+h+1]={false};
	scanf("%lf",&nun[h]);
	for(int i=1;i<m;i++){
		scanf("%d ",&b);
		scanf("%lf",&nun[b]);
	}
	for(int i=0;i<k+1;i++){
		if(num[i]!=0.0){
			for(int j=0;j<h+1;j++){
				if(nun[j]!=0.0){
					sum[i+j]+=num[i]*nun[j];
					if(vis[i+j]==false)
					set++;
					vis[i+j]=true;
				}
			}
		}
	}
	printf("%d",set);
	for(int i=k+h;i>=0;i--){
		if(vis[i]==true)
		printf(" %d %.1lf",i,sum[i]);
	
	}
	return 0;
	
} 
