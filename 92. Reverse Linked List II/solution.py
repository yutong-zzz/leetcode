# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None or head.next is None or m==n:
            return head
        dummy_node = ListNode(0)
        dummy_node.next = head
        p = dummy_node
        for i in range(m):
            fix_start = p
            p = p.next
        for i in range(n-m):
            # reverse
            pre = p
            cur = pre.next
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        fix_end = cur
        fix_start.next = pre
        p.next = fix_end
        head = dummy_node.next
        return head



# test
head=ListNode(1);
p1=ListNode(1);
p2=ListNode(2); 
p3=ListNode(3); 
head.next=p1; 
p1.next=p2; 
p2.next=p3; 
s = Solution()
p=s.reverseBetween(head,2,3); 
while p: 
  print p.val; 
  p=p.next;

print 'end'