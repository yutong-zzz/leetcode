# 83. Remove Duplicates from Sorted List
1. 用迭代法，确定新表头

if cur.val != cur.next.val：表头不变，继续迭代
else：寻找重复的最后一个node，以此node为head迭代

### TODO: 2. 直接建立不重复的新表