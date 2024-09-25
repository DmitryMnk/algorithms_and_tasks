from typing import Optional


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

    temp = ListNode()
    add = temp

    while list1 and list2:
        if list1.val > list2.val:
            add.next = list2
            list2 = list2.next
        else:
            add.next = list1
            list1 = list1.next

        add = add.next

    if list1:
        add.next = list1
    else:
        add.next = list2

    return temp.next

node_13 = ListNode(3)
node_12 = ListNode(4, node_13)
node_11 = ListNode(2, node_12)

node_23 = ListNode(4)
node_22 = ListNode(6, node_23)
node_21 = ListNode(5, node_22)

print(merge_two_lists(
    node_11,
    node_21
).next)