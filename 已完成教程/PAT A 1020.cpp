#include<iostream>
#include<queue>
#include<algorithm> 
using namespace std;

const int maxn=32;
struct node{
	int id;
	node *lchild,*rchild;
};
int pre[maxn],in[maxn],post[maxn],n,num=0;

node* create(int postL,int postR,int inL,int inR){
	if(postL>postR||inL>inR){
		return NULL;
	}else{
		node *root=new node;
		root->id=post[postR];
		int k;
		for(k=inL;k<=inR;++k){
			if(in[k]==root->id)
				break;
		}
		int numLeft=k-inL;
		root->lchild=create(postL,postL+numLeft-1,inL,k-1);
		root->rchild=create(postL+numLeft,postR-1,k+1,inR);
		return root;
	}
}
void BFS(node *root){
	queue<node*> q;
	q.push(root);
	while(!q.empty()){
		node *temp=q.front();
		q.pop();
		cout<<temp->id;
		++num;
		if(num<n)
			cout<<" ";
		if(temp->lchild!=NULL)
			q.push(temp->lchild);
		if(temp->rchild!=NULL)
			q.push(temp->rchild);
	}
}
int main(){
	cin>>n;
	getchar();
	for(int i=0;i<n;++i){
		cin>>post[i];
	}
	getchar();
	for(int i=0;i<n;++i){
		cin>>in[i];
	}
	getchar();
	node *root=create(0,n-1,0,n-1);
	BFS(root);
	return 0;
}
