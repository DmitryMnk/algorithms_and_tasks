from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    table = dict()

    while headA is not None:
        table[headA] = 1
        headA = headA.next

    while headB is not None:
        if table.get(headB):
            return headB
        headB = headB.next
    return None


node6 = ListNode(5)
node5 = ListNode(4)
node5.next = node6

node4= ListNode(8)
node4.next = node5

node3 = ListNode(1)
node3.next = node4

node2 = ListNode(1)
node2.next = node4

node1 = ListNode(6)
node1.next = node2

head1 = ListNode(4)
head1.next = node3

head2 = ListNode(5)
head2.next = node1

print(
    getIntersectionNode(
        head1, head2
    )
)
