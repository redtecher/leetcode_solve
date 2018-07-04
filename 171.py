class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        
        result = 0
        for i in range(length):
           result = result + (26**(length-i-1))*(ord(s[i])-ord('A')+1)
        return result    
        

if __name__=='__main__':    
    sl =Solution()
    
    s='ZY'
    print(sl.titleToNumber(s))