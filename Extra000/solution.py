class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

def reverselist(ll):
    cur = ll
    pre = None
    l = ll
    while cur:
        l = cur
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return l

# test
head=ListNode(1);
p1=ListNode(2);
p2=ListNode(3); 
p3=ListNode(4); 
head.next=p1; 
p1.next=p2; 
p2.next=p3; 
p=reverselist(head); 
while p: 
  print p.val; 
  p=p.next;