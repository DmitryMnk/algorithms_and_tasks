from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    p_stack = deque()
    q_stack = deque()
    p_node = p
    q_node = q
    while True:
        # if p_node and q_node:
        #     print(p_node, q_node)
        #     if p_node.val != q_node.val:
        #         return False
        #     p_stack.append(p_node)
        #     q_stack.append(q_node)
        #     p_node = p_node.left
        #     q_node = q_node.left
        # elif not p_node and not q_node:
        #     if p_stack and q_stack:
        #         p_node = p_stack.pop()
        #         q_node = q_stack.pop()
        #         p_node = p_node.right
        #         q_node = q_node.right
        #     elif not p_stack and not q_stack:
        #         return True
        #     else:
        #         return False
        # else:
        #     return False

        if not p and not q:
            return True
        elif not p or not q:
            return False
        return p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

node13 = TreeNode(val=15)
node12 = TreeNode(val=5)
head1 = TreeNode(val=10, left=node12, right=node13)

node23 = TreeNode(val=15)
node22 = TreeNode(val=5, right=node23)
head2 = TreeNode(val=10, left=node22)

print(
    is_same_tree(
        head1,
        head2
    )
)