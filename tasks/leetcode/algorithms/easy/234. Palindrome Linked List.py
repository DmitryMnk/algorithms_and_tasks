from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome(head: Optional[ListNode]) -> bool:
    numbers = []

    node = head

    while node is not None:
        numbers.append(node.val)
        node = node.next

    i = 0
    j = len(numbers) - 1

    while i <= j:
        if numbers[i] != numbers[j]:
            return False
        i += 1
        j -= 1
    return True