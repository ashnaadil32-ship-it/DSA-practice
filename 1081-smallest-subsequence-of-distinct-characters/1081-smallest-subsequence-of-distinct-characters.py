class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Count the total occurrences of each character
        last_occurrence = {char: i for i, char in enumerate(s)}
        
        stack = []
        seen = set()
        
        for i, char in enumerate(s):
            # If the character is already in our result stack, skip it
            if char in seen:
                continue
                
            # Greedy check: Pop characters from the stack if:
            # - The current character is smaller than the stack's top character
            # - The stack's top character appears again later in the string
            while stack and char < stack[-1] and last_occurrence[stack[-1]] > i:
                removed_char = stack.pop()
                seen.remove(removed_char)
                
            # Add the current character to the stack and mark it as seen
            stack.append(char)
            seen.add(char)
            
        return "".join(stack)