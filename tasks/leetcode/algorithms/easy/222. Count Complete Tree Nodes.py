from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


def count_nodes(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    left = 0
    right = 0

    node = root
    while node:
        left += 1
        node = node.left

    node = root
    while node:
        right += 1
        node = node.right

    if left == right:
        return 2 ** left - 1

    return 1 + count_nodes(root.left) + count_nodes(root.right)


node5 = TreeNode(6)
node4 = TreeNode(5)
node3 = TreeNode(4)
node2 = TreeNode(3, left = node5)
node1 = TreeNode(2, left=node3, right=node4)

root = TreeNode(1, left=node1, right=node2)

print(
    count_nodes(root)
)