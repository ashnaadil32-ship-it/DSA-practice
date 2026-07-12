class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # Total number of happy strings of length n is 3 * (2**(n-1))
        # If k is out of bounds, return an empty string
        total_happy_strings = 3 * (1 << (n - 1))
        if k > total_happy_strings:
            return ""
        
        # Adjust k to be 0-indexed for easier partition arithmetic
        k -= 1
        
        # We build the string character by character
        result = []
        choices = ['a', 'b', 'c']
        
        # Determine the first character
        partition_size = 1 << (n - 1)
        first_char_idx = k // partition_size
        result.append(choices[first_char_idx])
        
        # Update k for the remaining characters
        k %= partition_size
        
        # Determine the remaining n-1 characters
        for i in range(1, n):
            partition_size >>= 1  # Equivalent to dividing by 2
            
            # Filter available choices based on the previous character
            available_choices = [c for c in choices if c != result[-1]]
            
            char_idx = k // partition_size
            result.append(available_choices[char_idx])
            
            k %= partition_size
            
        return "".join(result)