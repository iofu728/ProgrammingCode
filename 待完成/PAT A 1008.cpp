#include"stdio.h"  
#include"string.h"  
#include"math.h"  
#include<iostream>  
#include<vector>  
#include<queue>  
#include<string>  
#include<algorithm>  
using namespace std;  
#define INF 0x7FFFFFFF  
  
vector<int> requests;  
int main(){  
    int num;  
    while(scanf("%d",&num) != EOF){  
        requests.resize(num);  
        int sum = 0;  
        for(int i = 0;i < num;i++){  
            int temp;  
            scanf("%d",&temp);  
            requests[i] = temp;  
        }  
        int nowStairs = 0;  
        for(int i = 0;i < num;i++){     //travel each request!  
            if(requests[i] > nowStairs){  
                sum += (requests[i] - nowStairs)*6;  
                nowStairs = requests[i];  
            }  
            if(requests[i] < nowStairs){  
                sum += (nowStairs-requests[i])*4;  
                nowStairs = requests[i];  
            }  
        }  
        //add the waiting time of each floor and output  
        printf("%d",sum+num*5);  
    }  
    return 0;  
}  
