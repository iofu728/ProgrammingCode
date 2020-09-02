/*
 * @Author: gunjianpan
 * @Date:   2020-09-02 16:48:57
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2020-09-02 16:48:59
 */

class Solution {
  public void wiggleSort(int[] nums) {
    for (int ii = 1; ii < nums.length; ++ii) {
      if ((ii >> 1 << 1 == ii && nums[ii] < nums[ii - 1]) ||
          (ii >> 1 << 1 != ii && nums[ii] > nums[ii - 1])) {
        int tmp = nums[ii - 1];
        nums[ii - 1] = nums[ii];
        nums[ii] = tmp;
      }
    }
  }
}