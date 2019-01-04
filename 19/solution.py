# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)  
        dummy.next = head
        p, q = dummy, dummy
        for i in range(n):
            p = p.next

        while p.next:
            p = p.next
            q = q.next

        del_node = q.next
        q.next = del_node.next
        del del_node
        return dummy.next

