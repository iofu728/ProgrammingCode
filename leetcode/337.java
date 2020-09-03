/*
 * @Author: gunjianpan
 * @Date:   2020-09-03 19:14:41
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2020-09-03 19:14:42
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
  public int rob(TreeNode root) {
    int[] res = dfs(root);
    return Math.max(res[0], res[1]);
  }

  public int[] dfs(TreeNode r) {
    if (r == null) {
      return new int[] {0, 0};
    }
    int[] left = dfs(r.left);
    int[] right = dfs(r.right);
    int v1 = left[1] + right[1] + r.val;
    int v2 = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);
    return new int[] {v1, v2};
  }
}