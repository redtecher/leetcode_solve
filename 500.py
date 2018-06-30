class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        firstline = ['q','w','e','r','t','y','u','i','o','p']
        secondline = ['a','s','d','f','g','h','j','k','l']
        thirdline = ['z','x','c','v','b','n','m']
        result = []
        for i in words:
            
            right = 0
            k=i.lower()
            
            if k[0]  in firstline :
                flag = 1
                
            if k[0]  in secondline :
                flag = 2
                
            if k[0]  in thirdline:
                flag = 3
                
            

            for j in range(1,len(k)):
                
                if k[j]  in firstline :
                    if flag==1:
                        right=0
                        continue
                    else:
                        right=1
                        break
                if k[j]  in secondline:
                    if flag==2:
                        right=0
                        continue
                    else:
                        right=1
                        break
                if k[j]  in thirdline:
                    if flag==3:
                        right=0
                        continue
                    else:
                        right=1
                        break
            if right==0:
                result.append(i)
        
        return result
                
            
        


if __name__=='__main__':
    sl=Solution()
    words = ["Hello", "Alaska", "Dad", "Peace"]
    sl.findWords(words)