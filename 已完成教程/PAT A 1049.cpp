#include<iostream>
int main(){
	int n,left=0,now=1,right=0,temp=0,bit=1;
	scanf("%d",&n);
	while(n/bit){
		left=n/(bit*10);
		now=(n/bit)%10;
		right=n%bit;
		if(!now){
			temp+=left*bit;
		}else if(now==1){
			temp+=left*bit+right+1;
		}else{
			temp+=(left+1)*bit;
		}
		bit*=10;
	}
	printf("%d",temp);
	return 0;
}