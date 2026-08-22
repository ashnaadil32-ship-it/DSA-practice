class Solution:
    def sortString(self,s):
        s1 = list(s)
        s1.sort()
        return "".join(s1)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        for word in strs:
            key = self.sortString(word)
            if key in freq:
                freq[key].append(word) 
            else:
                freq[key] = [word]  
        return list(freq.values())