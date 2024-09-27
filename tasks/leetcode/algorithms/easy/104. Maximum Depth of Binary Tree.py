from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


def max_depth(root: Optional[TreeNode]) -> int:

    def diving(node, current_depth):
        if node:
            return max(diving(node.left, current_depth + 1), diving(node.right, current_depth + 1))
        return current_depth

    return diving(root, 0)

node4 = TreeNode(val=7)
node3 = TreeNode(val=15)
node2 = TreeNode(val=20, left=node3, right=node4)
node1 = TreeNode(val=9)
head = TreeNode(val=3, left=node1, right=node2)

print(max_depth(
    head
))