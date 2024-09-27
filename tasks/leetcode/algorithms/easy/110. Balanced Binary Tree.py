from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


def is_balanced(root: Optional[TreeNode]) -> bool:
    def diving(l_node, r_ode2, current_depth1, current_depth2):
        ...




node4 = TreeNode(val=7)
node3 = TreeNode(val=15)
node2 = TreeNode(val=20, left=node3, right=node4)
node1 = TreeNode(val=9)
head = TreeNode(val=3, left=node1, right=node2)

print(is_balanced(head))