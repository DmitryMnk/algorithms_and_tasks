from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumOfLeftLeaves(root: Optional[TreeNode]) -> int:

    stack = deque()
    stack.append(root)
    total_sum = 0

    while stack:
        node = stack.pop()
        if node.right:
             stack.append(node.right)

        if node.left:
            stack.append(node.left)
            if node.left.left is None and node.left.right is None:
                total_sum += node.left.val

    return total_sum


node4 = TreeNode(val=7)
node3 = TreeNode(val=15)
node2 = TreeNode(val=20, left=node3, right=node4)
node1 = TreeNode(val=9)
root = TreeNode(3, left=node1, right=node2)

print(
    sumOfLeftLeaves(root)
)