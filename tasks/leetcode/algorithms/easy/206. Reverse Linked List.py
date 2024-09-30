from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}'

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:

    prev = None
    node = head
    while node is not None:
        curr = node.next
        node.next = prev
        prev = node
        node = curr
    return prev


node6 = ListNode(val=7)
node5 = ListNode(6, next=node6)
node4 = ListNode(5, next=node5)
node3 = ListNode(4, next=node4)
node2 = ListNode(3, next=node3)
node1 = ListNode(2, next=node2)
head = ListNode(1, next=node1)

new_head = reverseList(head)

while new_head is not None:
    print(new_head.val, end=' ')
    new_head = new_head.next