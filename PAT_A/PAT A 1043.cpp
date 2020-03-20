#include <cstdio>
#include <vector>
using namespace std;
const int maxn = 1001;
vector<int> orgin, pre, premirror, post, postmirror;
int n, m;
struct node {
  int data;
  node* lchlid;
  node* rchild;
};

node* newNode(int x) {
  node* root = new node;
  root->data = x;
  root->lchlid = root->rchild = NULL;
  return root;
}
void insert(node*& root, int x) {
  if (root == NULL) {
    root = newNode(x);
    return;
  }
  if (root->data > x) {
    insert(root->lchlid, x);
  } else
    insert(root->rchild, x);
}
node* create(int data[], int n) {
  node* root = NULL;
  for (int i = 0; i < n; i++) {
    insert(root, data[i]);
  }
  return root;
}
int num = 0;
void preorder(node* root) {
  if (root == NULL) return;
  pre.push_back(root->data);
  preorder(root->lchlid);
  preorder(root->rchild);
}
void premirrororder(node* root) {
  if (root == NULL) return;
  premirror.push_back(root->data);
  premirrororder(root->rchild);
  premirrororder(root->lchlid);
}
void postorder(node* root) {
  if (root == NULL) return;
  postorder(root->lchlid);
  postorder(root->rchild);
  post.push_back(root->data);
}
void postmirrororder(node* root) {
  if (root == NULL) return;
  postmirrororder(root->rchild);
  postmirrororder(root->lchlid);
  postmirror.push_back(root->data);
}
int data[maxn];
int main() {
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d", &data[i]);
    orgin.push_back(data[i]);
  }
  node* root = create(data, n);
  preorder(root);
  premirrororder(root);
  postorder(root);
  postmirrororder(root);
  if (pre == orgin) {
    printf("YES\n");
    for (int i = 0; i < post.size(); i++) {
      printf("%d", post[i]);
      if (i < post.size() - 1) printf(" ");
    }
  } else if (premirror == orgin) {
    printf("YES\n");
    for (int i = 0; i < postmirror.size(); i++) {
      printf("%d", postmirror[i]);
      if (i < postmirror.size() - 1) printf(" ");
    }
  } else
    printf("NO\n");
  return 0;
}
