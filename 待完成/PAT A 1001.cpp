#include<cstdio>
#include<cstdlib> 

int main(){
	int a,b,c;
	scanf("%d %d",&a,&b);
	c=a+b;
	if(c<1000&&c>-1000){
		printf("%d",c);
	}
	else if(c>1000000||c<-1000000){
		printf("%d,%03d,%03d",c/1000000,abs((c%1000000)/1000),abs((c%1000000)%1000)); 
	}
	else printf("%d,%03d",c/1000,abs(c%1000));
	return 0; 
}
