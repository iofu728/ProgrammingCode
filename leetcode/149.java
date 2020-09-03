/*
 * @Author: gunjianpan
 * @Date:   2020-09-03 00:04:18
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2020-09-03 00:04:21
 */

class Solution {
  public int maxPoints(int[][] points) {
    int N = points.length;
    if (N <= 2) {
      return N;
    }
    int res = 2;
    for (int ii = 0; ii < N; ++ii) {
      int x1 = points[ii][0], y1 = points[ii][1];
      Map<String, Integer> tmp = new HashMap<String, Integer>();
      int c_d = 0, h_l = 1;
      for (int jj = ii + 1; jj < N; ++jj) {
        int x2 = points[jj][0], y2 = points[jj][1];
        if (x1 == x2 && y1 == y2) {
          c_d += 1;
        } else if (y1 == y2) {
          h_l += 1;
        } else {
          int d = gcd(x1 - x2, y1 - y2);
          int dx = (x1 - x2) / d, dy = (y1 - y2) / d;
          String k = String.format("%d,%d", dx, dy);
          tmp.put(k, tmp.getOrDefault(k, 1) + 1);
        }
      }
      int now = 0;
      for (int k : tmp.values()) {
        now = Math.max(now, k);
      }
      now = Math.max(now, h_l) + c_d;
      res = Math.max(res, now);
    }
    return res;
  }

  public int gcd(int a, int b) {
    if (b != 0) {
      return gcd(b, a % b);
    }
    return a;
  }
}
