from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
            self.val = val
            self.next = next


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    temp = ListNode(0)
    head = temp
    carry = 0
    while l1 is not None or l2 is not None or carry != 0:
        digit1 = l1.val if l1 is not None else 0
        digit2 = l2.val if l2 is not None else 0

        summ = digit1 + digit2 + carry

        digit, carry = summ % 10, summ // 10
        temp.next = ListNode(digit)
        temp = temp.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    res = head.next
    head.next = None
    return res



node_13 = ListNode(3)
node_12 = ListNode(4, node_13)
node_11 = ListNode(2, node_12)

node_23 = ListNode(4)
node_22 = ListNode(6, node_23)
node_21 = ListNode(5, node_22)


node = add_two_numbers(node_11, node_21)

while node is not None:
    print(node.val, end=', ')
    node = node.next