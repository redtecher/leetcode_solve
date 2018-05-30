#开始做的时候脑袋混乱，，后来重构二叉树解决了。。把数值往后累计到叶子，还得考虑很多方面，递归还是好用啊


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        return self.newpathsum(root,sum,0)
    

    def newpathsum(self ,p , sum,n):
        
        p.val=p.val+n
        if p.left==None and p.right==None:
            if p.val ==sum:
                return True
            else:
                return False
        else:
        
        #if root.left==None and root.right==None:
            if not p.left==None:
                k=self.newpathsum(p.left,sum,p.val)
            else:
                k=False

            if p.right!=None:
                l=self.newpathsum(p.right,sum,p.val)   
            else :
                l=False

        if k==True or l==True:
            return True
        else:
            return False
        
            
        
            
            

    
            
         
        





if __name__=="__main__":
    sl = Solution()

    start = TreeNode(5)
    p1=TreeNode(4)
    p2=TreeNode(8)
    start.left=p1
    start.right=p2
    p1.left=TreeNode(1)
    p1.right=None
    p2.left=TreeNode(7)
    p2.right=TreeNode(11)
    print(sl.hasPathSum(start,11))
    
        