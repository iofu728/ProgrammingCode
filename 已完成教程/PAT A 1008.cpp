#include<cstdio>


int main(){
	
	int n;
	scanf("%d",&n);
	int num[n];
	for(int i=0;i<n;i++){
		scanf("%d",&num[i]);
	}
	int now=0,sum=0;
	for(int i=0;i<n;i++){
		if(now<num[i]){
			sum+=(num[i]-now)*6;
			now=num[i];
		}
		else{
			sum+=(now-num[i])*4;
			now=num[i];
		}
	}
	printf("%d",sum+n*5);
	return 0;
}
