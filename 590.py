"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root == None:
            return []
        res = []
        
        if root.children ==None:
            res.append(root.val)
            return res
        
        for child in root.children:
            res.extend(self.postorder(child))
        res.append(root.val)
        return res



if __name__=='__main__':
    sl =Solution()

    five =Node(5,None)
    six = Node(6,None)
    three = Node(3,[five,six])
    two = Node(2,None)
    four = Node(4,None)
    root = Node(1,[three,two,four])

    print(sl.postorder(root))