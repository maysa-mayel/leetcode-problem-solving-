class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        l= sentence.split(' ')
        last=l[-1][-1]
        for i in range (len(l)):
            if l[i][0]==last :
                last=l[i][-1]
            else:
                return False 
        return True
                
        