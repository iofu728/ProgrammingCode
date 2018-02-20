#include <iostream>
#include<vector>
#include<algorithm> 
using namespace std;

struct node{
	long long num;
	int rank,localrank,score,loca;
};
bool cmp(node a,node b){
	return (a.score==b.score)?(a.num<b.num):(a.score>b.score);
}
int main(int argc, char const *argv[])
{
	int n,id=1;
	cin>>n;
	getchar();
	vector<node> fin;
	for(int i=0;i<n;++i){
		int m;
		vector<node> v;
		cin>>m;
		getchar();
		if(m){
			for(int j=0;j<m;++j){
				node temp;
				temp.loca=id;
				cin>>temp.num>>temp.score;
				v.push_back(temp);
			}
			sort(v.begin(), v.end(),cmp);
			int r=2;
			v[0].localrank=1;
			for(int j=1;j<m;++j){
				v[j].localrank=(v[j].score==v[j-1].score)?(v[j-1].localrank):(r);
				++r;
			}
			fin.insert(fin.end(),v.begin(),v.end());
			++id;
		}
	}
	sort(fin.begin(), fin.end(),cmp);
	int r=2;
	fin[0].rank=1;
	for(int i=1;i<fin.size();++i){
		fin[i].rank=(fin[i].score==fin[i-1].score)?(fin[i-1].rank):(r);
		++r;
	}
	cout<<fin.size()<<endl;
	for(int i=0;i<fin.size();++i){
		node t=fin[i];
		printf("%013lld",t.num);
		cout<<" "<<t.rank<<" "<<t.loca<<" "<<t.localrank<<endl;
	}	
	return 0;
}
