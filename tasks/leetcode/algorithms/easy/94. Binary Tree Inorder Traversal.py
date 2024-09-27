from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


def inorder_traversal(root: Optional[TreeNode]) -> List[int]:

    # answer = list()
    # queue = deque()
    # node = root
    # while True:
    #     if node:
    #         queue.append(node)
    #         node = node.left
    #     else:
    #         if not queue:
    #             break
    #         node = queue.pop()
    #         answer.append(node.val)
    #         node = node.right
    # return answer

    res = []

    def inorder(root):
        if root is None:
            return
        inorder(root.left)
        res.append(root.val)
        inorder(root.right)

    inorder(root)

    return res

node3 = TreeNode(val=3)
node2 = TreeNode(val=2, left=node3)
head = TreeNode(val=1, right=node2)

print(inorder_traversal(
    head
))