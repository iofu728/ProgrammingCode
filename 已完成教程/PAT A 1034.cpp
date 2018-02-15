#include<iostream>
#include<map>
#include<string>
#include<algorithm>
using namespace std;
const int maxn=2018;
struct node
{
	int id,num;
	string str;
	
};
vector<node> v;
map<string, int> stringid;
map<int,string> idstring;

int co=0;
bool vis[maxn];
int G[maxn][maxn],weight[maxn];
int generateid(string str){
	if(stringid.find(str)==stringid.end()){
		stringid[str]=(co);
		idstring[co]=str;
		return co++;
	}else{
		return stringid[str];
	}
}
void DFS(int u,int &father,int &num,int &totalwight){
	++num;
	vis[u]=true;
	if(weight[u]>weight[father]){
		father=u;
	}
	for (int i = 0; i < co; ++i)
	{
		int temp=G[u][i];
		if(G[u][i]){
			totalwight+=G[u][i];
			G[u][i]=G[i][u]=0;
			if(vis[i]==false){
				DFS(i,father,num,totalwight);
			}

		}
		
	}
}
bool cmp(node a,node b){
	return a.str<b.str;
}
int main(int argc, char const *argv[])
{
	int n,k;
	cin>>n>>k;
	getchar();
	fill(vis,vis+maxn,false);
	fill(G[0],G[0]+maxn*maxn,0);
	fill(weight,weight+maxn,0);
	for (int i = 0; i < n; ++i)
	{
		int temp,id1,id2;
		string str1,str2;
		cin>>str1>>str2>>temp;
		id1=generateid(str1);
		id2=generateid(str2);
		G[id1][id2]+=temp;
		G[id2][id1]+=temp;
		weight[id1]+=temp;
		weight[id2]+=temp;
//		cout<<id1<<" "<<id2<<" "<<weight[id1]<<" "<<weight[id2]<<endl;
	}
//	for(int i=0;i<co;++i){
//		for(int j=0;j<co;++j){
//			cout<<G[i][j]<<" ";
//		}
//		cout<<endl;
//	}
	for(int i=0;i<co;++i){
		if(!vis[i]){
			int father=i,num=0,totalwight=0;
			DFS(i,father,num,totalwight);
//			cout<<father<<" "<<num<<" "<<totalwight<<endl;
			if(num>2&&totalwight>k){
//				cout<<"****";
				node temp;
				temp.id=father;
				temp.str=idstring[father];
				temp.num=num;
				v.push_back(temp);
			}
		}
	}
	cout<<v.size()<<endl;
	sort(v.begin(), v.end(),cmp);
	for(int i=0;i<v.size();++i){
		cout<<v[i].str<<" "<<v[i].num<<endl;
	}
	return 0;
}
