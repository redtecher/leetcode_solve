class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length=0
        m_length=0
        tempstring = []
        string_length = len(s)
        for i in range(string_length):
            if s[i] in tempstring:
                if m_length>max_length:
                    max_length=m_length
                # print(max_length,s[i])
                while tempstring[0]!=s[i]:
                    tempstring.pop(0)
                    m_length=m_length-1
                tempstring.pop(0)
                tempstring.append(s[i])
                # print("重构后:",tempstring,m_length)
                continue
                
            m_length=m_length+1
            tempstring.append(s[i])
            # print(tempstring,m_length)
        # print(max_length)
        if m_length>max_length:
            
            max_length = m_length
        return max_length

if __name__=='__main__':
    sl=Solution()

    s="abcabcaa"
    print(sl.lengthOfLongestSubstring(s))