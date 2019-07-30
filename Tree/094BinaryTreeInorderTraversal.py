# 94 Binary Tree Inorder Traversal

# recursive
class solution():
    def InorderTraversal(Self, root):
        res = []
        self.dfs (root, res)
        return res
    
    def dfs(self, root, res):
        if not root: return 
        self.dfs(root.left, res)
        res.append(root.val)
        self.dfs(root.right, res)

# stack
class solution1():
    def InorderTraversal1(Self, root):
        if not root: return []
            res, q = [], []
            self.leftintoStack(root, q)
            while q:
                tmp = q.pop()
                res.append(tmp.val)
                if tmp.right:
                leftintoStack(tmp.right, q)
        return res

    def leftintoStack(self, root, q):
        while root:
            q.append(root)
            root = root.left

# stackII left-> node-> right
class solution():
    def InorderTraversal2(Self, root):
        stack, res = [],[]
        while root:
            stack.append(root)
            root = root.left
        if not stack: return res
        root = stack.pop()
        res.append(root.val)
        root = root.right