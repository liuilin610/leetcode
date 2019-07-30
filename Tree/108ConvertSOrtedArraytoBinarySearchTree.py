# 108 Convert Sorted Array to Binary Tree

# not only one solution

class solution(object):
    def SortedArraytoBST(self, nums):
        """
        : type nums : List[int]
        : rtype : TreeNode
        """
        if not nums: return None
        L = len(nums)
        mid = L //2
        root = TreeNode(nums[mid])
        root.left = self.SortedArraytoBST(num[:mid])
        root.right = self.SortedArraytoBST(nums[mid+1:])
        return root

#
class solution(object):
    def SortedArraytoBST(self, nums):
        """
        : type nums : List[int]
        : rtype : TreeNode
        """
        def BuildTree(L,R):
            if L > R : return None
            mid = (L +R) >> 1
            root = TreeNode(nums[mid])
            root.left = BuildTree(L, mid-1)
            root.right = BuildTree(mid+1, R)
        return root
    return BuildTree(0, len(nums)-1)