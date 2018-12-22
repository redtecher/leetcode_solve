# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # addresult=0
        carryflag=0
        addresult = l1.val+l2.val
        if addresult>=10:
            addresult=addresult-10
            carryflag=1
            
        head = ListNode(addresult)
        resultlist = head
        l1=l1.next
        l2=l2.next
        
        
        while l1!=None and l2!=None:
            addresult = l1.val+l2.val+carryflag
            carryflag=0
            if addresult>=10:
                addresult=addresult-10
                carryflag=1
            resultlist.next=ListNode(addresult)
            l1=l1.next
            l2=l2.next
            resultlist=resultlist.next
        # self.printalllist(head)
        
        if l1==None:
            while l2!=None:
                addresult=l2.val+carryflag
                if l2.val+carryflag>=10:
                    addresult=addresult-10
                    carryflag=1
                else:
                    carryflag=0
                resultlist.next=ListNode(addresult)
                l2=l2.next
                resultlist=resultlist.next
                
        if l2==None:
            while l1!=None:
                addresult=l1.val+carryflag
                if l1.val+carryflag>=10:
                    addresult=addresult-10
                    carryflag=1
                else:
                    carryflag=0
                
                resultlist.next=ListNode(addresult)
                l1=l1.next
                resultlist=resultlist.next
        if carryflag==1:
            resultlist.next=ListNode(1)
        print("结果是:",end="")
        self.printalllist(head)

        return head
        
    def printalllist(self,l):
        while l.next!=None:
            print(l.val,"->",end="")
            l=l.next
        print(l.val)

        
        





if __name__=='__main__':
    sl=Solution()
    l1=ListNode(2)
    l1.next=ListNode(4)
    l1.next.next=ListNode(3)

    l2=ListNode(5)
    l2.next=ListNode(6)
    l2.next.next=ListNode(6)
    l2.next.next.next = ListNode(7)
    # l1=ListNode(5)
    # l2=ListNode(5)
    # resultlist=l1
    sl.addTwoNumbers(l1,l2)
    
            