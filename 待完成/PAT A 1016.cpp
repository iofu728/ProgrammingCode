#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;

int rate[24],n;
struct node{
	string name;
	int moth;
	int day;
	int hour;
	int minute;
	bool vis;
	
};
vector<node> v,sum;

bool cmp(node &a,node &b){
	if(a.name==b.name) {
		if(a.moth==b.moth){
			if(a.day==b.day){
				if(a.hour==b.hour){
					if(a.minute==b.minute){
						return a.vis>b.vis;
					}
					return a.minute<b.minute;
				}
				return a.hour<b.hour;
			}
			return a.day<b.day;
		}
		return a.moth<b.moth;
	}
	else return a.name<b.name;
}

double spend(int &minute){
	double spend=0;
	int tempday=sum[0].day,temphour=sum[0].hour,tempmin=sum[0].minute;
	do{
		if(tempday==sum[1].day&&temphour==sum[1].hour){
			minute+=(sum[1].minute-tempmin);
			spend+=rate[temphour]*(sum[1].minute-tempmin)*1.0/100;
			break;
		}
		else{
			spend+=rate[temphour]*(60.0-tempmin)*1.0/100;
			minute+=(60-tempmin);
		}
		tempmin=0;
		if(temphour==23) {
//			cout<<"****"<<" "<<tempday<<endl;
			tempday+=1;	
			temphour=0;	
		}
		else temphour+=1;
	}while(tempday<=sum[1].day&&temphour<=sum[1].hour);
	return spend;
}
int main(){
	for(int i=0;i<24;++i){
		cin>>rate[i];
	}
	cin>>n;
	for(int i=0;i<n;++i){
		string sign;
		node temp;
		cin>>temp.name;
		cin.get();
		cin>>temp.moth;
		cin.get();
		cin>>temp.day;
		getchar();
		cin>>temp.hour;
		cin.get();
		cin>>temp.minute;
		cin.get();
		cin>>sign;
		if(sign.size()==7) temp.vis=true;
		else temp.vis=false;
		v.push_back(temp);
	}
	sort(v.begin(),v.end(),cmp);
//	for(int i=0;i<v.size();++i){
//		cout<<v[i].name<<" "<<v[i].vis<<" "<<v[i].day<<" "<<v[i].hour<<" "<<v[i].minute<<endl;
//	}
//	
	string name;
	double total=0;
	for(int i=0;i<v.size();++i){
		if(sum.size()==0&&v[i].vis==true){
			if(name!=v[i].name)
				{	
//				cout<<1<<endl;
					if(total!=0) {
						printf("Total amount: $%.2lf\n",total);
						total=0;
					}
					name=v[i].name;
					cout<<v[i].name<<" ";
					printf("%02d\n",v[i].moth);
				 } 
			sum.push_back(v[i]);
	
		}
		else if(sum.size()==1){

			if(v[i].vis==true){
//				cout<<3<<endl;				
				sum.clear();
				sum.push_back(v[i]);
			}
			else{
//				cout<<4<<endl;
				sum.push_back(v[i]); 
				int minute=0;
				double fill=spend(minute);
				total+=fill;
				printf("%02d:%02d:%02d %02d:%02d:%02d %d $%.2lf\n",sum[0].day,sum[0].hour,sum[0].minute,sum[1].day,sum[1].hour,sum[1].minute,minute,fill);
				sum.clear();
				 
			}
			
		} 
	}
	printf("Total amount: $%.2lf\n",total);
	return 0;
	
} 
