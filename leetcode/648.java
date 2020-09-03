/*
 * @Author: gunjianpan
 * @Date:   2020-09-03 22:20:30
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2020-09-03 22:20:31
 */

class Solution {
  public String replaceWords(List<String> dictionary, String sentence) {
    TrieNode trie = new TrieNode();
    for (String s : dictionary) {
      TrieNode cur = trie;
      for (char c : s.toCharArray()) {
        if (cur.children[c - 'a'] == null) {
          cur.children[c - 'a'] = new TrieNode();
        }
        cur = cur.children[c - 'a'];
      }
      cur.word = s;
    }
    StringBuilder res = new StringBuilder();
    for (String s : sentence.split("\\s+")) {
      if (res.length() > 0) {
        res.append(" ");
      }
      TrieNode cur = trie;
      for (char c : s.toCharArray()) {
        if (cur.children[c - 'a'] == null || cur.word != null) {
          break;
        }
        cur = cur.children[c - 'a'];
      }
      res.append(cur.word == null ? s : cur.word);
    }
    return res.toString();
  }
}

class TrieNode {
  TrieNode[] children;
  String word;
  TrieNode() { children = new TrieNode[26]; }
}
