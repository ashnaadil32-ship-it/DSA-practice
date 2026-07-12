class Solution:
    def twoEditWords(self, queries: list[str], dictionary: list[str]) -> list[str]:
        ans = []
        
        for q in queries:
            for d in dictionary:
                # Count the number of differing characters at identical indices
                mismatches = sum(1 for c1, c2 in zip(q, d) if c1 != c2)
                
                # If the word can be matched within 2 edits, it's valid
                if mismatches <= 2:
                    ans.append(q)
                    break # Move to the next query word immediately
                    
        return ans