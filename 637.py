# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = []
        if root.left==None and root.right==None:
            res.append(root.val)
            print("子节点")
            print(root.val)
            return res
        else:
            res.append(root.val)
            leftnum = self.averageOfLevels(root.left)
            rightnum =self.averageOfLevels(root.right)
            # print(leftnum)
            # print(rightnum)
            # lengthleft = len(leftnum)
            # lengthright = len(rightnum)
            # if lengthleft>lengthright:
            #     length = lengthleft
            #     for i in range(lengthright,lengthleft):
            #         rightnum.append(0)

            # else:
            #     length = lengthright
            #     for i in range(lengthleft,lengthright):
            #         leftnum.append(0)
            

            for i in range(length):
                res.append((leftnum[i]+rightnum[i])/2)

            return res
            


            


            
            


if __name__=='__main__':
    sl = Solution()
    three = TreeNode(3)
    nine = TreeNode(9)
    twenty = TreeNode(20)
    fifteen = TreeNode(15)
    seven = TreeNode(7)
    three.left = nine
    three.right=twenty
    twenty.left=fifteen
    twenty.right=seven


    print(sl.averageOfLevels(three))
        