from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


def preorderTraversal(root: Optional[TreeNode]) -> List[int]:

    if root is None:
        return []

    queue = deque()
    queue.append(root)
    result = list()
    while queue:
        node = queue.pop()
        result.append(node.val)

        if node.right is not None:
            queue.append(node.right)

        if node.left is not None:
            queue.append(node.left)


    return result


node8 = TreeNode(val=9)
node7 = TreeNode(val=7)
node6 = TreeNode(val=6)
node5 = TreeNode(val=8, left = node8)
node4 = TreeNode(val=5, left=node6, right=node7)
node3 = TreeNode(val=4)
node2 = TreeNode(val=3, right=node5)
node1 = TreeNode(val=2, left=node3, right=node4)
head = TreeNode(val=1, left=node1, right=node2)

print(preorderTraversal(head))