class Solution {
  public List<List<Integer>> threeSum(int[] nums) {
    int n = nums.length;
    Arrays.sort(nums);
    List<List<Integer>> ans = new ArrayList<List<Integer>>();
    // 枚举 a
    for (int first = 0; first < n; ++first) {
      // 需要和上一次枚举的数不相同
      if (first > 0 && nums[first] == nums[first - 1]) {
        continue;
      }
      // c 对应的指针初始指向数组的最右端
      int third = n - 1;
      int target = -nums[first];
      // 枚举 b
      for (int second = first + 1; second < n; ++second) {
        // 需要和上一次枚举的数不相同
        if (second > first + 1 && nums[second] == nums[second - 1]) {
          continue;
        }
        // 需要保证 b 的指针在 c 的指针的左侧
        while (second < third && nums[second] + nums[third] > target) {
          --third;
        }
        // 如果指针重合，随着 b 后续的增加
        // 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
        if (second == third) {
          break;
        }
        if (nums[second] + nums[third] == target) {
          List<Integer> list = new ArrayList<Integer>();
          list.add(nums[first]);
          list.add(nums[second]);
          list.add(nums[third]);
          ans.add(list);
        }
      }
    }
    return ans;
  }
}

class Solution {
  public List<List<Integer>> threeSum(int[] nums) {
    int n = nums.length;
    int count = 0;
    Arrays.sort(nums);
    List<Integer> temp = new ArrayList<Integer>();
    List<List<Integer>> s = new ArrayList<List<Integer>>();
    // ArrayList 和List用法区别，真是醉了？？？

    for (int i = 0; i < n; i++) {
      int target = 0 - nums[i];
      // z只经n-1~j遍历,和j的遍历同时
      //时间复杂度n2
      int z = n - 1;
      if (i > 0 && nums[i] == nums[i - 1])
        continue;
      for (int j = i + 1; j < n; j++) {
        // j和i 可以一样。但是不可以和上一个循环的j一样
        if (nums[j] == nums[j - 1] && j > i + 1) {
          continue;
        }
        while (nums[j] == nums[z] || nums[j] + nums[z] > target)
          z--;
        if (nums[j] + nums[z] == target) {
          List<Integer> tmp = new ArrayList<Integer>();
          temp.add(nums[i]);
          temp.add(nums[j]);
          temp.add(nums[z]);
          s.add(temp);
          System.out.print(temp);
          System.out.print(s);
          // System.out.print(i);
          // System.out.print(j);
          // System.out.print(z);
          System.out.print(' ');
          // count++;
          break;
        }
      }
    }

    return s;
  }
}