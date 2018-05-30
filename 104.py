# Definition for a binary tree node.
#模拟二叉树  递归了。。不过开始没考虑那个最大值，折腾了半天最后ac了。
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def maxDepth(self, root):
        if root==None:
            return 0
        """
        :type root: TreeNode
        :rtype: int
        """
        
        
        
        
        p=root
        if p.left == None and p.right == None:
            
            return 1
            
        else:
            rileng=self.maxDepth(p.right)+1
        
            leleng=self.maxDepth(p.left)+1
            return max(rileng,leleng)
            
        




if __name__=='__main__':
    sl = Solution()
    tn=TreeNode([])

    sl.maxDepth(tn)
    