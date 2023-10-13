# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 이진검색트리에서 두 노드간 가장 최소 차이
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        global minval
        minval = 999999

        def preorder(node):
            global minval
            if not node:
                return

            x = search(node)
            if minval > x:
                minval = x
            preorder(node.left)
            preorder(node.right)

            return minval

        def search(node):
            if not node:
                return 999999
            
            if node.left and node.right:
                a = left_node(node.left)
                b = right_node(node.right)
               
                if (node.val - a) > (b - node.val):
                    return (b-node.val)
                else:
                    return (node.val-a)
            elif node.left and not node.right:
                c = left_node(node.left)
                return (node.val-c)
            elif not node.left and node.right:
                d = right_node(node.right)
                return (d-node.val)
            else:
                return 999999

        def left_node(node):
            if node.right:
                return left_node(node.right)
            else:
                return node.val

        def right_node(node):
            if node.left:
                return right_node(node.left)
            else:
                return node.val

        return preorder(root)