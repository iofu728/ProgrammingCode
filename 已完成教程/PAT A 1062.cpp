#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
struct node
{
	int id,virtue,talent,sum;
};
bool cmp(node a,node b){
	return (a.sum==b.sum)?((a.virtue==b.virtue)?(a.id<b.id):(a.virtue>=b.virtue)):(a.sum>b.sum);
}
vector<node> sages,noblemen,fool,v;
int main(){
	int n,l,h;
	cin>>n>>l>>h;
	getchar();
	for(int i=0;i<n;++i){
		node temp;
		cin>>temp.id>>temp.virtue>>temp.talent;
		if(temp.virtue>=l&&temp.talent>=l){
			temp.sum=temp.talent+temp.virtue;
			if(temp.virtue>=h){
				if(temp.talent>=h){
					sages.push_back(temp);
				}else{
					noblemen.push_back(temp);
				}
			}else{
				if(temp.virtue>=temp.talent){
					fool.push_back(temp);	
				}else{
					v.push_back(temp);
				}
			}
		}
	}
	cout<<(sages.size()+noblemen.size()+fool.size()+v.size())<<endl;
	sort(sages.begin(), sages.end(),cmp);
	sort(noblemen.begin(), noblemen.end(),cmp);
	sort(fool.begin(), fool.end(),cmp);
	sort(v.begin(),v.end(),cmp);
	for(int i=0;i<sages.size();++i){
		node temp=sages[i];
		printf("%05d %d %d\n",temp.id,temp.virtue,temp.talent);
	}
	for(int i=0;i<noblemen.size();++i){
		node temp=noblemen[i];
		printf("%05d %d %d\n",temp.id,temp.virtue,temp.talent);
	}	
	for(int i=0;i<fool.size();++i){
		node temp=fool[i];
		printf("%05d %d %d\n",temp.id,temp.virtue,temp.talent);
	}	
	for(int i=0;i<v.size();++i){
		node temp=v[i];
		printf("%05d %d %d\n",temp.id,temp.virtue,temp.talent);
	}
	return 0;
} 
