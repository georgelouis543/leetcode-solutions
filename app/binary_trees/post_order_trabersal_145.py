# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out_list = []

        def post_order_dfs(node):
            if not node:
                return None

            post_order_dfs(node.left)
            post_order_dfs(node.right)
            out_list.append(node.val)

        post_order_dfs(root)
        return out_list