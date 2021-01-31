1. N叉树的后序遍历

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        #递归出口
        if not root:
            return []
        res = []
        for i in root.children:
            res.extend(self.postorder(i))
        res.append(root.val)
        return res

2. N叉树的前序遍历

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        #递归出口
        if not root:
            return []
        res = []
        res.append(root.val)
        for i in root.children:
            res.extend(self.preorder(i))
        return res

3. 二叉树的中序遍历

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#二叉树遍历
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        #递归出口
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


4. 二叉树的前序遍历

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

5. N叉树的层序遍历

6. 前K个高频元素


