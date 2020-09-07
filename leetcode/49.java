/*
 * @Author: gunjianpan
 * @Date:   2020-09-06 14:26:21
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2020-09-06 14:26:31
 */

class Solution {
  public List<List<String>> groupAnagrams(String[] strs) {
    if (strs.length == 0)
      return new ArrayList();
    Map<String, List> ans = new HashMap<String, List>();
    for (String s : strs) {
      char[] ca = s.toCharArray();
      Arrays.sort(ca);
      // String key = ca.toString();
      String key = String.valueOf(ca);
      // System.out.println(key);
      if (!ans.containsKey(key))
        ans.put(key, new ArrayList());
      ans.get(key).add(s);
    }
    return new ArrayList(ans.values());
  }
}