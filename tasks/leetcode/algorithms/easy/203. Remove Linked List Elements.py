from typing import Optional



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}'


def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    # if not head:
    #     return None
    # nodes = [ListNode(0)]
    # node = head
    # while node is not None:
    #     if node.val != val:
    #         nodes[-1].next = node
    #         nodes.append(node)
    #     else:
    #         nodes[-1].next = None
    #     node = node.next
    # if len(nodes) > 1:
    #     return nodes[1]
    # return None

    new_head = ListNode()
    temp = new_head
    node = head
    while node is not None:
        if node.val != val:
            temp.next = node
            temp = node
        else:
            temp.next = None
        node = node.next
    return new_head.next


node6 = ListNode(val=6)
node5 = ListNode(5, next=node6)
node4 = ListNode(4, next=node5)
node3 = ListNode(3, next=node4)
node2 = ListNode(6, next=node3)
node1 = ListNode(2, next=node2)
head = ListNode(1, next=node1)

new_head = removeElements(head, 6)

while new_head is not None:
    print(new_head.val, end=' ')
    new_head = new_head.next