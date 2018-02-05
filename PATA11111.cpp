class maxsum
{
public:
	 int generatesum(vector<int> A,int n){
	 	int sum=0;
	 	int max=0;
	 	for(int i=0;i<n;++i){
	 		if(max>=0)
	 		max=sum>max?sum:max;
	 	else sum=0;
	 	}
	 	return max;


	 }
	
};