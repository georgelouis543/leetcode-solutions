# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out_list = []

        def dfs_in_order(node):
            if not node:
                return None

            dfs_in_order(node.left)
            out_list.append(node.val)
            dfs_in_order(node.right)

        dfs_in_order(root)
        return out_list
