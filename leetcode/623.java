/*
 * @Author: gunjianpan
 * @Date:   2020-09-02 16:08:36
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2020-09-02 16:08:40
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
  public TreeNode addOneRow(TreeNode root, int v, int d) {
    TreeNode f = root;
    Queue<TreeNode> queue = new LinkedList<TreeNode>();
    queue.add(root);
    int h = 1;
    while (h < d - 1) {
      Queue<TreeNode> tmp = new LinkedList<TreeNode>();
      while (!queue.isEmpty()) {
        TreeNode top = queue.remove();
        if (top.left != null) {
          tmp.add(top.left);
        }
        if (top.right != null) {
          tmp.add(top.right);
        }
      }
      queue = tmp;
      ++h;
    }
    if (d == 1) {
      TreeNode now = new TreeNode(v);
      now.left = f;
      return now;
    }
    for (TreeNode ii : queue) {
      TreeNode left = new TreeNode(v);
      TreeNode right = new TreeNode(v);
      left.left = ii.left;
      right.right = ii.right;
      ii.left = left;
      ii.right = right;
    }
    return f;
  }
}
