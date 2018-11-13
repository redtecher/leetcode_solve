class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        result = []
        for email in emails:
            solve = email.split('@')[0].replace('.','')
            for i in range(len(solve)):
                if solve[i]=='+':
                    break
            solve= solve[:i]
            newsolve =solve+'@'+email.split('@')[1]
            
            flag=0
            for i in result:
                if newsolve==i :
                    
                    flag= 1
            if flag==0:
                result.append(newsolve)

        return len(result)
        

        

if __name__ =="__main__":
    sl =Solution()
    emails= ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    sl.numUniqueEmails(emails)