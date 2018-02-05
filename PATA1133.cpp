#include<cstdio>
#include<vector>
using namespace std;
const int maxn=99999;
struct node{
	int nextid;
	int data;
}G[maxn];
int n,m,k;
vector<int> prez,inz,postz;

int main(){
	scanf("%d %d %d",&n,&m,&k);
	for(int i=0;i<m;i++){
	int id,nid,data;
	scanf("%d%d%d",&id,&data,&nid);
	G[id].data=data;
	G[id].nextid=nid;	
	}
	int id=n;
	for(int i=0;i<m;i++){
		if(G[id].data<0) prez.push_back(id);
		else if(G[id].data>k) postz.push_back(id);
		else inz.push_back(id);
		id=G[id].nextid;
	}
	for(int i=0;i<prez.size();i++){
		printf("%05d %d ",prez[i],G[prez[i]].data);
		if(i+1<prez.size()) printf("\n%05d\n",prez[i+1]);
		else if(inz.size()!=0) printf("%05d\n",inz[0]);
		else if(postz.size()!=0) printf("%05d\n",postz[0]);
		else printf("-1\n");
	}
	for(int i=0;i<inz.size();i++){
		printf("%05d %d ",inz[i],G[inz[i]].data);
		if(i+1<inz.size()) printf("%05d\n",inz[i+1]);
		else if(postz.size()!=0) printf("%05d\n",postz[0]);
		else printf("-1\n");
	}
	for(int i=0;i<postz.size();i++){
		printf("%05d %d ",postz[i],G[postz[i]].data);
		if(i+1<postz.size()) printf("%05d\n",postz[i+1]);
		else printf("-1\n");
	}

	return 0;
}
