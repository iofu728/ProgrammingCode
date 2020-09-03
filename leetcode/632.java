/*
 * @Author: gunjianpan
 * @Date:   2020-09-03 17:03:48
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2020-09-03 17:03:50
 */

class Solution {
  public int[] smallestRange(List<List<Integer>> nums) {
    int res_min = 0, res_max = Integer.MAX_VALUE;
    int max_v = Integer.MIN_VALUE, min_v;
    int n = nums.size();
    int[] next = new int[n];
    PriorityQueue<Integer> queue =
        new PriorityQueue<Integer>(new Comparator<Integer>() {
          public int compare(Integer a, Integer b) {
            return nums.get(a).get(next[a]) - nums.get(b).get(next[b]);
          }
        });
    for (int i = 0; i < n; ++i) {
      queue.offer(i);
      max_v = Math.max(max_v, nums.get(i).get(0));
    }
    while (true) {
      int index = queue.poll();
      if (max_v - nums.get(index).get(next[index]) < res_max - res_min) {
        res_max = max_v;
        res_min = nums.get(index).get(next[index]);
      }
      ++next[index];
      if (next[index] == nums.get(index).size()) {
        break;
      }
      queue.offer(index);
      max_v = Math.max(max_v, nums.get(index).get(next[index]));
    }
    return new int[] {res_min, res_max};
  }
}
