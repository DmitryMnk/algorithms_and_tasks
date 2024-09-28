from collections import deque
from typing import Optional
from unittest.mock import right


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    if not root:
        return False

    queue = deque()
    queue.append([root, 0])
    while queue:
        node, prev_sum = queue.popleft()
        current_sum = prev_sum + node.val
        if current_sum == target_sum and node.left is None and node.right is None:
            return True
        if node.left:
            queue.append([node.left, current_sum])

        if node.right:
            queue.append([node.right, current_sum])

    return False

node8 = TreeNode(1)
node7 = TreeNode(2)
node6 = TreeNode(7)
node5 = TreeNode(4, right=node8)
node4 = TreeNode(13)
node3 = TreeNode(11, left=node6, right=node7)
node2 = TreeNode(8, left=node4, right=node5)
node1 = TreeNode(4, left=node3)
root = TreeNode(5, left=node1, right=node2)

print(
    has_path_sum(
        root, 26
    )
)
