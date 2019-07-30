# 105 COnstruct Binary Tree from Preorder and Inorder

class solution(object):
    def ConstructBSTPreIn(self,preorder,inorder):
        """
        : type preorder : List[int]
        : type inorder : List[int]
        : rtype : TreeNode
        """
        if not preorder: return None
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        root.left = self.ConstructBSTPreIn(preorder[1: index+1], inorder[: index])
        root.right = self.ConstructBSTPreIn(preorder[index+1:], inorder[index+1:])
        return root


# II we can reset the index to increase the efficiency
#left.subtree [pi+1,pi+len+1) [ii, ii+len)
#right.subtree [pi+len+1, pd) [ii+len+1, id)
class solution(object):
    def ConstructBSTPreIn1(self,preorder, inorder):
        """
        : type preorder : List[int]
        : type inorder : List[int]
        : rtype : TreeNode
        """
        return self.Construct(0, len(preorder), 0, len(inorder), preorder, inorder)

        def Construct(self,pi,pd,ii,id,preorder,inorder):
        if pi >= pd or ii >= id : return None
        root = TreeNode(preorder[pi])
        len_left = inner.index(preorder[pi]) - ii
        root.left = self.Construct(pi+1, pi+len_left+1, ii, ii+len_left, preorder, inorder)
        root.right = self.Construct(pi+len_left+1, pd, ii+len_left+1, id, preorder, inorder)
        return root
    

