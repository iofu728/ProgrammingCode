#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
const int maxn=1000l;
int n;

struct node{
	char id[16];
	int hh1,mm1,ss1;
	int hh2,mm2,ss2;
}NODE[maxn];
bool cmp1(node a,node b){
	if(a.hh1==b.hh1){
		if(a.mm1==b.mm1){
			return a.ss1<b.ss1;
		}
		return a.mm1<b.mm1;
		
	}
	return a.hh1<b.hh1;
}
bool cmp2(node a,node b){
	if(a.hh2==b.hh2){
		if(a.mm2==b.mm2){
			return a.ss2>b.ss2;
		}
		return a.mm2>b.mm2;
		
	}
	return a.hh2>b.hh2;
}

 int main(){
 	
 	scanf("%d",&n);
 	
 	for(int i=0;i<n;i++){
 		scanf("%s %d:%d:%d %d:%d:%d",&NODE[i].id,&NODE[i].hh1,&NODE[i].mm1,&NODE[i].ss1,&NODE[i].hh2,&NODE[i].mm2,&NODE[i].ss2);
 		
	 }
	 
	sort(NODE,NODE+n,cmp1);
	printf("%s ",NODE[0].id);
	sort(NODE,NODE+n,cmp2);
	printf("%s",NODE[0].id);
	return 0;
 }
