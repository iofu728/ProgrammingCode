/*
 * @Author: gunjianpan
 * @Date:   2020-09-03 15:22:51
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2020-09-03 15:22:53
 */

class Solution {
  public boolean searchMatrix(int[][] matrix, int target) {
    int n = matrix.length;
    if (n == 0) {
      return false;
    }
    int m = matrix[0].length;
    int left = 0, right = n * m - 1;
    while (left <= right) {
      int mid = (left + right) >> 1;
      int x = mid / m, y = mid % m;
      if (matrix[x][y] == target) {
        return true;
      }
      if (matrix[x][y] > target) {
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    }
    return false;
  }
}
