#coding=utf-8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        dummy_node = ListNode(0)
        dummy_node.next = head

        pre = dummy_node
        cur = pre.next
        insert_pos = dummy_node   # pre node of insertion
        find_ins = 0
        while cur:
            if cur.val >= x and not find_ins:
                insert_pos = pre
                find_ins = 1
            elif cur.val < x and find_ins:
                pre.next = cur.next  # 调整原节点连接
                new_node = cur               #
                tmp = insert_pos.next        #
                insert_pos.next = new_node   # 调整新节点位置连接
                new_node.next = tmp          #

                insert_pos = insert_pos.next     # update pre node of insertion
                find_ins = 0
            pre = cur
            cur = cur.next
            
        head = dummy_node.next
        return head



# test
head=ListNode(1)
p1=ListNode(4)
p2=ListNode(3) 
p3=ListNode(2) 
p4=ListNode(5) 
p5=ListNode(2) 
head.next=p1
p1.next=p2
p2.next=p3
p3.next = p4
p4.next = p5
s = Solution()
p=s.partition(head,3)
while p: 
  print p.val
  p=p.next

print 'end'