class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        result = []
        for i in range(len(S)):
            left = S[i-len(S)::-1].find(C)
            right  = S[i:].find(C)
            print(left,right)
            if left==-1:
                left = 10001
            if right==-1:
                right = 10001
            result.append(min(left,right)) 
        return result

                
                
        



if __name__=='__main__':
    sl=Solution()
    S = "loveleetcode"
    C = 'e'
    print(sl.shortestToChar(S,C))