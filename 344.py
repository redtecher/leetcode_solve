class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        list1 = list(s)
        
        list1.reverse()
        s = "".join(list1)
        
        return s
        


if __name__=='__main__':
    sl = Solution()
    s="hello"
    sl.reverseString(s)