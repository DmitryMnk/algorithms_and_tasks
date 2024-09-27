from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


def is_balanced(root: Optional[TreeNode]) -> bool:
    def dfs(root):
        if root is None:
            return [True, 0]

        left, right = dfs(root.left), dfs(root.right)
        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

        return [balanced, 1 + max(left[1], right[1])]

    return dfs(root)[0]


node4 = TreeNode(val=7)
node3 = TreeNode(val=15)
node2 = TreeNode(val=20, left=node3, right=node4)
node1 = TreeNode(val=9)
head = TreeNode(val=3, left=node1, right=node2)

print(is_balanced(head))