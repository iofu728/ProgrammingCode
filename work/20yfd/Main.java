/*
 * @Author: gunjianpan
 * @Date:   2020-10-24 19:52:35
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2020-10-24 20:04:48
 */

// 本题为考试多行输入输出规范示例，无需提交，不计分。
import java.util.*;

public class Main {
  pr
  public static void dfs(int[] s, int tmp, int len, List<Integer> list,
                         int[] vis) {
    if (len == s.length) {
      list.add(tmp);
      return;
    }
    for (int i = 0; i < s.length; i++) {
      if (vis[i] == 1)
        continue;
      else if (len == 0 && s[i] == 0)
        continue;
      vis[i] = 1;
      dfs(s, tmp * 10 + s[i], len + 1, list, vis);
      vis[i] = 0;
    }
  }

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int k = sc.nextInt();
    List<Integer> list = new ArrayList<>();
    int[] vis = new int[n];
    int[] s = new int[n];
    for (int i = 0; i < n; i++) {
      s[i] = sc.nextInt();
    }
    Arrays.sort(s);
    dfs(s, 0, 0, list, vis);
    
    for (int i = 0; i < list.size(); i++) {
      System.out.println(list.get(i));
      // if (list.get(i) % k == 0) {
      //   System.out.print(list.get(i));
      //   return;
      // }
    }
  }
}