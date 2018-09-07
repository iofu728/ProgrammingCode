#include <algorithm>
#include <iostream>
using namespace std;
struct node {
  int data, height;
  node *left, *right;
};
node *newNode(int num) {
  node *root = new node;
  root->data = num;
  root->height = 1;
  root->left = root->right = NULL;
  return root;
}
int getheight(node *root) {
  if (root == NULL) return 0;
  return root->height;
}
int getbalance(node *root) {
  return getheight(root->left) - getheight(root->right);
}
int update(node *&root) {
  root->height = max(getheight(root->left), getheight(root->right)) + 1;
}
void L(node *&root) {
  node *temp = root->right;
  root->right = temp->left;
  temp->left = root;
  update(root);
  update(temp);
  root = temp;
}
void R(node *&root) {
  node *temp = root->left;
  root->left = temp->right;
  temp->right = root;
  update(root);
  update(temp);
  root = temp;
}
node insert(node *&root, int num) {
  if (root == NULL) {
    root = newNode(num);
  } else if (root->data > num) {
    insert(root->left, num);
    update(root);
    if (getbalance(root) == 2) {
      if (getbalance(root->left) == 1) {
        R(root);
      } else if (getbalance(root->left) == -1) {
        L(root->left);
        R(root);
      }
    }
  } else {
    insert(root->right, num);
    update(root);
    if (getbalance(root) == -2) {
      if (getbalance(root->right) == -1) {
        L(root);
      } else if (getbalance(root->right) == 1) {
        R(root->right);
        L(root);
      }
    }
  }
}
node *create(int n) {
  int num;
  node *root = NULL;
  for (int i = 0; i < n; ++i) {
    scanf("%d", &num);
    insert(root, num);
  }
  return root;
}
int main() {
  int n;
  scanf("%d", &n);
  node *root = create(n);
  printf("%d\n", root->data);
  return 0;
}
