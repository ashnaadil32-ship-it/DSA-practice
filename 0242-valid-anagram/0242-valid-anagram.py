class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       if len(s) != len(t):
          return False
       count1 = {}
       count2 = {}

       for ch in s:
        if ch in count1:
            count1[ch] += 1  
        else :
            count1[ch] = 1

       for ch in t:
        if ch in count2:
            count2[ch] += 1
        else:
            count2[ch] = 1

       return count1 == count2