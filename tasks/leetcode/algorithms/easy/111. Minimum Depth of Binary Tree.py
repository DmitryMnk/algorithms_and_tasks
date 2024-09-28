from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


def minimum_deep_tree(root: Optional[TreeNode]):
    if root is None:
        return 0

    # def diving(node: Optional[TreeNode]):
    #     if node is None:
    #         return float('inf')
    #     if node.left is None and node.right is None:
    #         return 1
    #     else:
    #         return 1 + min(diving(node.left), diving(node.right))
    #
    # return diving(root)

    queue = deque()
    queue.append([root, 1])
    while queue:
        node, depth = queue.popleft()
        if node.left is None and node.right is None:
            return depth
        if node.left is not None:
            queue.append([node.left, depth + 1])
        if node.right is not None:
            queue.append([node.right, depth + 1])




node4 = TreeNode(val=7)
node3 = TreeNode(val=15)
node2 = TreeNode(val=20, left=node3, right=node4)
node1 = TreeNode(val=9)
head = TreeNode(val=3, left=node1, right=node2)

print(
    minimum_deep_tree(head)
)