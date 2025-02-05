class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        x=[]
        if s1==s2:
            return True 
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                x.append(i)
        res=(len(x)==2) and s1[x[0]]==s2[x[1]] and s1[x[1]]==s2[x[0]] 
        return res                 