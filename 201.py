# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head==None:
            return None
        p=head
        while p!=None and p.val == val:
            p=p.next
        head =p
        #print(p.val)
        while p!=None and p.next!=None:
            
            

            if p.next.val==val:
                p.next = p.next.next
                
            else:
                p=p.next
            
    
            '''
            if p.next.next==None and p.next.val==val:
                p.next = None
                break
            '''
        return head
            
        


if __name__=='__main__':
    sl =Solution()
    head = ListNode(1)
    '''
    head.next = ListNode(2)
    head.next.next = ListNode(6)
    head.next.next.next = ListNode(6)
    '''
    sl.removeElements(head,1)
    