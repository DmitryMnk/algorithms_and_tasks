from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


def is_symmetric(root: Optional[TreeNode]):
    # l_node = root.left
    # r_node = root.right
    #
    # l_stack = deque()
    # r_stack = deque()
    #
    # while True:
    #     print(l_node, r_node)
    #     if l_node and r_node:
    #         if l_node.val != r_node.val:
    #             return False
    #         l_stack.append(l_node)
    #         r_stack.append(r_node)
    #         l_node = l_node.left
    #         r_node = r_node.right
    #     elif l_node or r_node:
    #         return False
    #     else:
    #         if not l_stack and not r_stack:
    #             return True
    #         elif not l_stack or not r_stack:
    #             return False
    #         else:
    #             l_node = l_stack.pop()
    #             r_node = r_stack.pop()
    #             l_node = l_node.right
    #             r_node = r_node.left
    if not root:
        return True


    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False

        return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)


    return is_mirror(root.left, root.right)

r_node_3 = TreeNode(val=3)
r_node_2 = TreeNode(val=4)
r_node_1 = TreeNode(val=2, left=r_node_2, right=r_node_3)

l_node_3 = TreeNode(val=4)
l_node_2 = TreeNode(val=3)
l_node_1 = TreeNode(val=2, left=l_node_2, right=l_node_3)
head = TreeNode(val=1, left=l_node_1, right=r_node_1)

print(
    is_symmetric(head)
)