# Definition for singly-linked list.
# 感觉做这种题就是得脑袋清晰。。。也就正常的链表查询删除
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head ==None:
            return head

        p= head
        while p.next!=None:
            if p.val==p.next.val :
                
                p.next=p.next.next
            else:
                p=p.next
         

        return head


if __name__=='__main__':
    sl = Solution()
    head = ListNode(1)
    head.next=ListNode(1)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(1)
    head = sl.deleteDuplicates(head)
    while head!=None:
        print(head.val)
        head= head.next     