class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        i = 0
        res = []
        
        # Split s into its independent special components
        for j, char in enumerate(s):
            if char == '1':
                count += 1
            else:
                count -= 1
                
            # A valid independent special component is found
            if count == 0:
                # Recursively process the inside of this component
                # Component layout: '1' + inner_content + '0'
                inner_content = self.makeLargestSpecial(s[i + 1:j])
                res.append('1' + inner_content + '0')
                i = j + 1
                
        # Sort the components in descending order to maximize lexicographical value
        res.sort(reverse=True)
        
        return "".join(res)