# 144 Binary Tree Preorder Traversal

# I recursive
# recursive left child then right child
class solution():
    def PreorderTraversal(slef, root):
        """
        : type root : TreeNode
        : rtype : List[int]
        """
        if not root: return None
        res = []
        res.append(root.val)
        res.extend(self.PreorderTraversal(root.left))
        res.extend(self.PreodrerTraversal(root.right))
        return res

# II- stack
# Final In Fisrt Out: right child in first
class solution1():
    def PreorderTraversal1(slef, root):
        """
        : type root : TreeNode
        : rtype : List[int]
        """
        if not root: return []
            res, stack = [], []
            stack.append(root)
        while stack:
            node = stack.pop()
            if not node:
                continue
            res.append(node.val)
            res.append(node.right)
            res.append(node.left)
        return res

    