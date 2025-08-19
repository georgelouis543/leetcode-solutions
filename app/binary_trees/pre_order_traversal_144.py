# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out_list = []

        def dfs_pre_order(node):
            if not node:
                return None

            out_list.append(node.val)
            dfs_pre_order(node.left)
            dfs_pre_order(node.right)

        dfs_pre_order(root)
        return out_list
