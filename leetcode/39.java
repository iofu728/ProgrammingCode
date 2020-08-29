class Solution {

  public void dfs(int[] s, int t, List<List<Integer>> res, List<Integer> temp,
                  int begin) {
    if (t == 0) {
      // System.out.print(temp);
      // System.out.print(t);
      System.out.print(" ");
      res.add(new ArrayList<>(temp));
      // System.out.print(temp);
      temp.clear();
      return;

    } else if (t < s[begin]) {
      temp.remove(temp.size() - 1);
      //  System.out.print(t);
      //  System.out.print(s[begin]);
      // System.out.print(temp);
      return;
    }

    // begin 防止查到前面去
    for (int i = begin; i < s.length; i++) {
      if (s[i] > t)
        break;
      if (s[i] <= t) {
        temp.add(s[i]);
        System.out.print(temp);
        System.out.print(t);
        // int[] b = Arrays.copyOfRange(s, i, s.length);
        dfs(s, t - s[i], res, temp, i);
      }
    }
    // return res;
  }
  public List<List<Integer>> combinationSum(int[] candidates, int target) {
    Arrays.sort(candidates);
    List<List<Integer>> res = new ArrayList<List<Integer>>();
    List<Integer> temp = new ArrayList<Integer>();
    dfs(candidates, target, res, temp, 0);

    return res;
  }
}