from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_paths(root: Optional[TreeNode]) -> List[str]:
    if not root:
        return []

    path = ''
    result = []
    stack = deque()
    stack.append([root, path])
    while stack:
        node, path = stack.pop()
        path += f'->{node.val}'
        if node.right is None and node.left is None:
            result.append(path[2:])

        if node.right:
            stack.append([node.right, path])

        if node.left:
            stack.append([node.left, path])


    return result




node6 = TreeNode(9)
node5 = TreeNode(6)
node4 = TreeNode(3)
node3 = TreeNode(1)
node2 = TreeNode(7, left = node5, right=node6)
node1 = TreeNode(2, left=node3, right=node4)
head = TreeNode(4, left=node1, right=node2)

print(
    binary_tree_paths(head)
)