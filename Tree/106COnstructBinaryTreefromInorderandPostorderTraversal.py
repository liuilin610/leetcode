# 106 COnstruct Binary Tree from Inorder and Postorder Traversal

class solution():
    def ConstructBSTPostIn(self, postorder, inorder):
        """
        : type inorder : List[int]
        : type postorder : List[int]
        : rtype : TreeNode 
        """
        if nor inorder or not postorder: return None
        val = postorder[-1]
        root = TreeNode(val)
        index = inorder.index(val)
        root.left = self.ConstructBSTPostIn(inorder[:index], postorder[: index])
        root.right = self.ConstructBSTPostIn(inorder[index+1:], postorder[index: -1])
        return root

# II
# left.subtree : [pi, pi+len) [ii, ii+len)
# right.subtree : [pi+len, pd-1] [ii+len+1, id)
class solution():
    def ConstructBSTPostIn(self, postorder, inorder):
        """
        : type inorder : List[int]
        : type postorder : List[int]
        : rtype : TreeNode 
        """
        return self.Construct1(0, len(postorder), 0, len(inorder), postorder, inorder)

    def Construct1(self, pi, pd, ii, id, preorder, inorder):
        if pi> pd or ii > id : return None
        root = TreeNode(postorder[pd-1])
        len_left = inorder.index(postorder[pd-1]) -ii
        root.left = self.Construct1(pi, pi_len_left, ii, ii+len_left, postorder, inorder)
        root.right = self.Construct1(pi+len_left, pd-1, ii+len_left, id, postorder, inorder)
        return root
