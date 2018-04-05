# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#recurse
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        p = head.next
        if p.val != head.val:
            head.next = self.deleteDuplicates(p)
            return head
        else:
            while p and p.val==head.val:
                p = p.next
            return self.deleteDuplicates(p)

# test
head=ListNode(1);
p1=ListNode(1);
p2=ListNode(2); 
p3=ListNode(3); 
head.next=p1; 
p1.next=p2; 
p2.next=p3; 
s = Solution()
p=s.deleteDuplicates(head); 
while p: 
  print p.val; 
  p=p.next;

print 'end'
                

