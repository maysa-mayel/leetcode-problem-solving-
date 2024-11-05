class Solution:
    def minChanges(self, s: str) -> int:
        min=0
        for i in range(0, len(s), 2):
            if s[i]!=s[i+1]:
                min+=1
        return min
            