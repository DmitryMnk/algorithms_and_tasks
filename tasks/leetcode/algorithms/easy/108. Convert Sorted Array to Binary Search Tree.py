from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'

def sorted_array_to_bst(nums: list[int]) -> Optional[TreeNode]:
    if not nums or len(nums) <= 0:
        return None

    if len(nums) == 1:
        leaf_node = TreeNode()
        leaf_node.val = nums[0]
        return leaf_node

    middle = len(nums) // 2

    head = TreeNode(
        val=nums[middle],
    )

    head.left = sorted_array_to_bst(nums[:middle])
    head.right = sorted_array_to_bst(nums[middle + 1:])

    return head

print(
    sorted_array_to_bst([-10,-3,0,5,9])
)