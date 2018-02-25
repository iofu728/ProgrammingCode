#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
const int maxn=100001; 
int times[maxn]={0},primes[maxn]={1};
int main(){
	fill(primes,primes+maxn,1);
	fill(times,times+maxn,0);
	for(int i=2;i*i<maxn;++i){
		for(int j=2;i*j<maxn;++j){
			primes[i*j]=0;
		}
	}
	int num;
	scanf("%d",&num);
	int now=num,id=2,c=0,v=0;
	if(num==1){
		printf("1=1\n");
	}else{
		while(now!=1){
			if(now%id==0&&primes[id]==1){
				++times[id];
				now/=id;
				++c;
			}else{
				++id;
			}
		}
		bool vis=false;
		cout<<num<<"=";
		for(int i=2;i<maxn&&v<c;++i){
			if(times[i]){
				++v;
				if(vis){
					cout<<"*";
				}else{
					vis=true;
				}
				cout<<i;
				if(times[i]>1){
					cout<<"^"<<times[i];
				}
			}
		}		
	}
	return 0;
}
