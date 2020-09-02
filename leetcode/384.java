/*
 * @Author: gunjianpan
 * @Date:   2020-09-02 09:48:35
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2020-09-02 09:48:41
 */

class Solution {
  public String decodeString(String s) {
    List<String> stack = new ArrayList<String>();
    List<Integer> nums = new ArrayList<Integer>();
    stack.add("");
    nums.add(1);
    int idx = 0;
    int N = s.length();
    int num;
    String tmp;
    while (idx < N) {
      char cur = s.charAt(idx);
      if (Character.isDigit(cur)) {
        int begin = idx;
        while (idx < N && Character.isDigit(s.charAt(idx))) {
          idx += 1;
        }
        num = Integer.parseInt(s.substring(begin, idx));
        stack.add("");
        nums.add(num);
      } else if (cur == ']') {
        num = nums.remove(nums.size() - 1);
        tmp = stack.remove(stack.size() - 1);
        System.out.printf("%d %s\n", num, tmp.repeat(num));
        stack.set(stack.size() - 1,
                  stack.get(stack.size() - 1) + tmp.repeat(num));
      } else if (cur == ']') {
        if (idx == 0 || !Character.isDigit(s.charAt(idx - 1))) {
          stack.add("");
          nums.add(1);
        }
      } else {
        stack.set(stack.size() - 1, stack.get(stack.size() - 1) + cur);
      }
      idx += 1;
    }
    return stack.remove(stack.size() - 1);
  }
}
