
class Solution {
  public String longestPalindrome(String s) {
    //暴力破解
    int n = s.length();
    int k = 0;
    int len = 0;
    int start = 0;
    for (int i = 0; i < n; i++) {
      for (int j = i + 1; j < n; j++) {
        // System.out.print(i+" "+j);

        if (len < (j - i + 1) && rev(s, i, j)) {
          System.out.print(i + " " + j);

          len = j - i + 1;
          start = i;
        }
      }
    }
    // System.out.print(start+" "+len);
    return s.substring(start, start + len);
  }

  private boolean rev(String s, int i, int j) {
    if (i >= j) {
      return true;
    }
    return s.charAt(i) == s.charAt(j) && rev(s, i + 1, j - 1);
  }
}
public class Solution {

  public String longestPalindrome(String s) {
    int len = s.length();
    if (len < 2) {
      return s;
    }

    int maxLen = 1;
    int begin = 0;
    // s.charAt(i) 每次都会检查数组下标越界，因此先转换成字符数组
    char[] charArray = s.toCharArray();

    // 枚举所有长度大于 1 的子串 charArray[i..j]
    for (int i = 0; i < len - 1; i++) {
      for (int j = i + 1; j < len; j++) {
        if (j - i + 1 > maxLen && validPalindromic(charArray, i, j)) {
          maxLen = j - i + 1;
          begin = i;
        }
      }
    }
    return s.substring(begin, begin + maxLen);
  }

  /**
   * 验证子串 s[left..right] 是否为回文串
   */
  private boolean validPalindromic(char[] charArray, int left, int right) {
    while (left < right) {
      if (charArray[left] != charArray[right]) {
        return false;
      }
      left++;
      right--;
    }
    return true;
  }
}