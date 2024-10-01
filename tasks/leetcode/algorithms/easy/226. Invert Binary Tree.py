from collections import deque
from typing import Optional

from dulwich.diff_tree import TreeChange



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


def print_tree(root: Optional[TreeNode]):

    stack = deque()
    stack.append(root)
    while stack:
        node = stack.pop()
        print(node.val, end=' ')
        if node.left:
            stack.append(node.left)

        if node.right:
            stack.append(node.right)

def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        stack = deque()
        stack.append(root)

        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

            node.left, node.right = node.right, node.left

        return root




node6 = TreeNode(9)
node5 = TreeNode(6)
node4 = TreeNode(3)
node3 = TreeNode(1)
node2 = TreeNode(7, left = node5, right=node6)
node1 = TreeNode(2, left=node3, right=node4)
head = TreeNode(4, left=node1, right=node2)

print_tree(head)
new_head = invert_tree(head)
print_tree(new_head)