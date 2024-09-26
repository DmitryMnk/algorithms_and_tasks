from typing import Optional



class ListNode:
    def __init__(self, val=0, next=None):
            self.val = val
            self.next = next


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    current = head.next
    temp = head
    while current is not None:
        if current.val != temp.val:
            temp.next = current
            temp = current
        current = current.next
    if current is None:
        temp.next = None
    return head

node_15 = ListNode(3)
node_14 = ListNode(3, node_15)
node_13 = ListNode(2, node_14)
node_12 = ListNode(1, node_13)
node_11 = ListNode(1, node_12)

result = delete_duplicates(node_11)
while result is not None:
    print(result.val, end = ',')
    result = result.next