class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numandroman = {
            'I':1,
        
            'V':5,
       
            'X':10,
      
            'L':50,

            'C':100,

            'D':500,
 
            'M':1000


        }

        result=0
        for i in range(len(s)-1):
            
            if numandroman[s[i]]<numandroman[s[i+1]]:
                result= result-numandroman[s[i]]
            else :
                result = result+numandroman[s[i]]
        return result+numandroman[s[-1]]
                            
            
        



if __name__=='__main__':
    sl= Solution()

    print(sl.romanToInt('LVIII'))

