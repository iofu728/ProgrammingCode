/*
 * @Author: gunjianpan
 * @Date:   2020-09-02 11:58:29
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2020-09-02 11:58:32
 */

class Solution {
  public int minTime(int[] time, int m) {
    int left = 0, right = 0, mid;
    for (int ii : time) {
      right += ii;
    }
    while (left < right) {
      mid = (left + right) >> 1;
      if (dfs(mid, time, m)) {
        right = mid;
      } else {
        left = mid + 1;
      }
    }
    return left;
  }

  public boolean dfs(int limit, int[] time, int m) {
    int total = 0, day = 1, max_v = time[0], now;
    for (int ii = 1; ii < time.length; ++ii) {
      now = time[ii];
      if (total + Math.min(max_v, now) <= limit) {
        total += Math.min(max_v, now);
        max_v = Math.max(max_v, now);
      } else {
        day += 1;
        total = 0;
        max_v = now;
      }
    }
    return day <= m;
  }
}
