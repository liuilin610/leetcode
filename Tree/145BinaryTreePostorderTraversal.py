# 145 Binary Tree Postorder Traversal

# stack
class solution():
    def PostTraversal( self, root):
        if not root : return[]
        res, q = [],[]
        q.append(root)
        while q :
            tmp = q.pop()
            if tmp.left, temp.right = q.append(root.left), q.append(root.right)
            res.append(tmp.val)

        return res[::-1]


# II -recursive
class solution():
    def PostTraversal1(self, root):
        res = []
        self.dfs(root, res):
        return res

    def dfs(self, root, res):
        if not root: return
        self.dfs(root.left, res)
        self.dfs(root.right, res)    
        res.append(root.val)
        
