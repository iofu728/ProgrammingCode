#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int main(){
	char a[10],b[10];
	int tag,radix,x=0,temp;
	int c[36][10],d[10];
	bool vis[36]={true},dan=false;
	scanf("%s %s",a,b);
	scanf("%d %d",&tag,&radix);
	if(tag==2)
	swap(a,b);
	//printf(" %d ",strlen(b));
	
	for(int i=0;i<strlen(a);i++){
		if(a[i]<='9'&&a[i]>='0'){
		x=x*radix+a[i]-'0';
		}
		if(a[i]<='z'&&a[i]>='a'){
		x=x*radix+a[i]-'a'+10;
		}			
		
	}
	//printf("%d ",x);
	for(int i=0;i<strlen(b);i++){
		if(b[i]<='9'&&b[i]>='0'){
		d[i]=b[i]-'0';
		}
		if(b[i]<='z'&&b[i]>='a'){
		d[i]=b[i]+10-'a';
		}			
		
	}


	for(int i=2;i<36;i++){
		vis[i]=true;
		temp=x;
		int j=0;
		while(temp){
			c[i][j]=temp%i;
			temp=temp/i;
			//if(c[i][j]==d[strlen(b)-j-1]){
			//	printf("YES");
			//}
			//else printf("NO");
			//printf("%d ",c[i][j]);
			//printf("%d ",d[strlen(b)-j-1]);
			if(c[i][j]==d[strlen(b)-j-1]);
			else{
				vis[i]=false;
				break;
			}
			if(vis[i]==false) break;
			j++;
		}

		if(vis[i]==true){
			
			dan=true;
			
		}
		
	}
	
	if(vis[10]==true){
		printf("10");
	}
	else if(vis[2]==true){
		printf("2");
	}
	else if(vis[16]==true){
		printf("16");
	}
	else if(dan==true){
		for(int i=3;i<36;i++){
			if(vis[i]==true){
				printf("%d",i);
				goto mp;
			}
		}
	}
	else
	printf("Impossible");
	mp:
	return 0;
		
}
