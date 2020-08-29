/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
  public void nlr(TreeNode root, TreeNode pre) {
    if (root != null) {
      pre.right = root;
      pre.left = null;
      pre = pre.right;
      System.out.println(pre.val + " " + root.val);

      nlr(root.left, pre);
      nlr(root.right, pre);
    }
  }
  public void flatten(TreeNode root) {
    TreeNode pre = new TreeNode(0);
    nlr(root, pre);
    root = pre.right;
  }
}

class Solution {
  public void flatten(TreeNode root) {
    List<TreeNode> list = new ArrayList<TreeNode>();
    preorderTraversal(root, list);
    int size = list.size();
    for (int i = 1; i < size; i++) {
      TreeNode prev = list.get(i - 1), curr = list.get(i);
      prev.left = null;
      prev.right = curr;
    }
  }

  public void preorderTraversal(TreeNode root, List<TreeNode> list) {
    if (root != null) {
      list.add(root);
      preorderTraversal(root.left, list);
      preorderTraversal(root.right, list);
    }
  }
}
