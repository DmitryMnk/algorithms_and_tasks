from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        stack = deque()
        stack.append(root)

        table = {}

        while stack:
            node = stack.popleft()
            table.setdefault(node.value, 0)
            table[node.value] += 1

            if node.left is not None:
                node.append(node.left)

            if node.right is not None:
                node.append(node.right)

        result = [0]

        for k, v in table.items():
            if v > result[0]:
                result = [k]
            elif v == table[result[0]]:
                result.append(k)
        return result