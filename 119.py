'''
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        currentlist=[]
        newlist = []
        for i in range(rowIndex+1):
            
            for j in range(i):
                if j==0:
                    newlist[0]=1
                    continue
                if j==len(currentlist):
                    newlist[-1]=1
                    continue
                newlist[j]=currentlist[j-1]+currentlist[j]
                print(newlist)
            currentlist=newlist
            newlist=[]
            print(currentlist)
        return currentlist
'''
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        p = [1]
        if not rowIndex:
            return p
        for j in range(rowIndex):
            p = [1] + [p[i]+p[i+1] for i in range(len(p)-1)] +[1]
        return p                              
                



if __name__=='__main__':
    sl = Solution()
    print(sl.getRow(3))