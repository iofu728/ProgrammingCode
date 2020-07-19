class Solution {
  public double findMedianSortedArrays(int[] nums1, int[] nums2) {
    // O(log(m + n))。
    //二分，每次在2个数组中去掉 中位值/2个数
    int m = nums1.length;
    int n = nums2.length;

    int left = (n + m + 1) / 2;
    int right = (n + m + 2) / 2;
    double mid1 = 0;
    double mid2 = 0;
    int s1 = 0;
    int s2 = 0;
    int e1 = m - 1;
    int e2 = n - 1;
    mid1 = findmid(nums1, nums2, left, s1, s2, e1, e2);
    mid2 = findmid(nums1, nums2, right, s1, s2, e1, e2);
    System.out.println(left + " " + right);
    System.out.println(mid1 + " " + mid2);

    return (mid1 + mid2) / 2;
  }

  private double findmid(int[] nums1, int[] nums2, int k, int s1, int s2,
                         int e1, int e2) {
    System.out.println(k + " " + s1 + " " + s2);
    double mid = 0;
    int len1 = e1 - s1 + 1;
    int len2 = e2 - s2 + 1;
    //让 len1 的长度小于 len2，这样就能保证如果有数组空了，一定是 len1
    if (len1 > len2)
      return findmid(nums2, nums1, k, s2, s1, e2, e1);
    if (len1 == 0) {
      System.out.println("==" + s2 + " " + k);
      return nums2[s2 + k - 1];
    }

    int a = k / 2;
    int a1 = s1 + a - 1;
    int a2 = s2 + a - 1;
    if (a1 > e1)
      a1 = e1; //中间位置
    if (a2 > e2)
      a2 = e2; //中间位置

    if (k == 1) {
      mid = nums1[s1] < nums2[s2] ? nums1[s1] : nums2[s2];
    } else {

      if (nums1[a1] <= nums2[a2]) {
        mid = findmid(nums1, nums2, k - (a2 - s2 + 1), a1 + 1, s2, e1, e2);
        System.out.println(" " + a1 + " " + a2);
      }

      else {
        mid = findmid(nums1, nums2, k - (a1 - s1 + 1), s1, a2 + 1, e1, e2);
        System.out.println(" " + a1 + " " + a2);
      }
    }

    return mid;
  }
}

