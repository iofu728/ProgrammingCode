/*
 * @Author: gunjianpan
 * @Date:   2020-09-03 20:01:08
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2020-09-03 20:01:10
 */

/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
  public Node copyRandomList(Node head) {
    if (head == null) {
      return head;
    }
    Node now = head;
    while (now != null) {
      Node new_node = new Node(now.val);
      new_node.next = now.next;
      now.next = new_node;
      now = new_node.next;
    }
    now = head;
    while (now != null) {
      now.next.random = now.random != null ? now.random.next : null;
      now = now.next.next;
    }
    Node origin = head;
    now = head.next;
    Node new_node = head.next;
    while (origin != null) {
      origin.next = origin.next.next;
      new_node.next = (new_node.next != null) ? new_node.next.next : null;
      origin = origin.next;
      new_node = new_node.next;
    }
    return now;
  }
}
