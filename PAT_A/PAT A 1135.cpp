#include <cmath>
#include <cstdio>
#include <queue>
#include <vector>
using namespace std;

const int maxn = 31;
struct node {
  int data, layer, num;
  bool vis;
  node *lchild, *rchild;
};
int num[maxn];

node* newnode(int x) {
  node* root = new node;
  if (x < 0) {
    root->vis = false;
    root->data = -x;
    root->lchild = root->rchild = NULL;
  } else {
    root->data = x;
    root->vis = true;
    root->lchild = root->rchild = NULL;
  }
  return root;
}
node* create(int L, int R) {
  if (L > R) return NULL;
  node* root = newnode(num[L]);
  int k = L + 1;
  while (k <= R && abs(num[k]) < abs(num[L])) k++;
  root->lchild = create(L + 1, k - 1);
  root->rchild = create(k, R);
  return root;
}
void BFSlayer(node* root) {
  queue<node*> q;
  root->layer = 1;
  root->num = 1;
  q.push(root);
  while (!q.empty()) {
    node* front = q.front();
    q.pop();
    if (front->lchild != NULL) {
      if (front->lchild->vis == true)
        front->lchild->num = front->num + 1;
      else
        front->lchild->num = front->num;
      front->lchild->layer = front->layer + 1;
      q.push(front->lchild);
    }
    if (front->rchild != NULL) {
      if (front->rchild->vis == true)
        front->rchild->num = front->num + 1;
      else
        front->rchild->num = front->num;
      front->rchild->layer = front->layer + 1;
      q.push(front->rchild);
    }
  }
  return;
}
bool BFSys(node* root) {
  vector<bool> layervis;
  queue<node*> q;
  q.push(root);
  int num = 0;
  while (!q.empty()) {
    node* front = q.front();
    q.pop();

    if (layervis.size() < front->layer) {
      layervis.push_back(front->vis);
      if (front->layer >= 2 && layervis[front->layer - 2] == false &&
          layervis[front->layer - 1] == false)
        return false;
    } else {
      if (layervis[front->layer - 1] != front->vis) return false;
    }
    if (front->lchild == NULL && front->rchild == NULL) {
      if (num == 0)
        num = front->num;
      else {
        if (num != front->num) return false;
      }
    }
    if (front->lchild != NULL) q.push(front->lchild);
    if (front->rchild != NULL) q.push(front->rchild);
  }

  return true;
}

int main() {
  int n, m;
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d", &m);
    for (int j = 0; j < m; j++) {
      scanf("%d", &num[j]);
    }
    node* root = create(0, m - 1);
    if (num[0] < 0)
      printf("No\n");
    else {
      BFSlayer(root);
      bool BFS = BFSys(root);
      if (BFS == true)
        printf("Yes\n");
      else
        printf("No\n");
    }
  }
  return 0;
}
