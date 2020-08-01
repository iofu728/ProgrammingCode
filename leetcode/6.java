/*
 * @Author: gunjianpan
 * @Date:   2020-07-20 23:06:08
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2020-07-20 23:15:56
 */
class Solution {
  public String convert(String s, int numRows) {
    if (numRows == 1)
      return s;

    int n = s.length();
    StringBuilder[] a = new StringBuilder[numRows];
    int p = numRows * 2 - 2;
    // System.out.print(s);
    // char[][] ch=new char[numRows][];

    for (int i = 0; i < n; i++) {
      // a[i%p].append(charAt(i));
      int j = i % p;
      System.out.print(a[0]);
      if (i % p < numRows) {
        if (a[j] == null) {
          a[j] = new StringBuilder();
        }
        a[j].append(s.charAt(i));
      }

      if (i % p >= numRows) {
        if (a[p - j] == null)
          a[p - j] = new StringBuilder();
        a[p - j].append(s.charAt(i));
      }
    }
    return ("12");

    //  System.out.println(a[i]);

    //  return(a);
  }
}