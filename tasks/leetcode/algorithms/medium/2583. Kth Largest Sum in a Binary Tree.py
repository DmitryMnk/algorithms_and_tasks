from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        stack = deque()
        stack.append((root, 1))
        table = {}

        while stack:
            node, level = stack.pop()
            table.setdefault(level, 0)
            table[level] += node.val

            if node.left:
                stack.append((node.left, level + 1))

            if node.right:
                stack.append((node.right, level + 1))
        values = table.values()
        if len(values) < k:
            return -1
        else:
            return sorted(values, reverse=True)[k - 1]

