from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def has_cycle(head: Optional[ListNode]) -> bool:
    table = {}

    node = head
    while True:
        if node is None:
            return False
        elif table.get(node) == 1:
            return True
        table[node] = 1
        node = node.next

node3 = ListNode(2)
node2 = ListNode(0)
node2.next = node3
node1 = ListNode(1)
node1.next = node2
head = ListNode(3)
head.next = node1

print(
    has_cycle(
        head
    )
)