/*
 * @Author: gunjianpan
 * @Date:   2020-09-03 09:59:34
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2020-09-03 09:59:36
 */

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
  public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
    dfs(t1, t2);
    if (t1 == null) {
      return t2;
    }
    return t1;
  }
  public void dfs(TreeNode t1, TreeNode t2) {
    if (t1 == null) {
      t1 = t2;
    } else if (t2 == null) {
      dfs(t1.left, t2);
      dfs(t1.left, t2);
    } else {
      t1.val = t1.val + t2.val;
      if (t1.left == null && t2.left != null) {
        t1.left = t2.left;
        t2.left = null;
      }
      if (t1.right == null && t2.right != null) {
        t1.right = t2.right;
        t2.right = null;
      }
      dfs(t1.left, t2.left);
      dfs(t1.right, t2.right);
    }
    return;
  }
}