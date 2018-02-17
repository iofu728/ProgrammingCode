#include <iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
	int n,m;
	cin>>n;
	getchar();
	vector<int> v(n);

	for(int i=0;i<n;++i){
		cin>>v[i];
	}
	getchar();
	cin>>m;
	getchar();
	vector<int> p(m);
	for(int i=0;i<m;++i){
		cin>>p[i];
	} 
	getchar();
	sort(v.begin(), v.end());
	sort(p.begin(), p.end());
	int i=0,j=n-1,k=m-1,sum=0;
	while(i<n&&i<m&&v[i]<0&&p[i]<0){
		sum+=v[i]*p[i];
		++i;
	}
	while(j>=0&&k>=0&&v[j]>0&&p[k]>0){
		sum+=v[j]*p[k];
		--j,--k;
	}
	cout<<sum<<endl;
	return 0;
}