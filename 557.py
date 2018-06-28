class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        slist =  s.split(" ")
        sresult = []
        for i in slist:
            newlist = list(i)
            newlist.reverse()
            strlist = "".join(newlist)
            sresult.append(strlist)
        
        result = " ".join(sresult)
        
        return result
        




if __name__=='__main__':
    sl =Solution()
    s="Let's take LeetCode contest"

    sl.reverseWords(s)