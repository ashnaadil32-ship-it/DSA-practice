class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        sample = "123456789"
        result = []
        
        # Get the character length bounds
        min_len = len(str(low))
        max_len = len(str(high))
        
        # Iterate through all possible lengths of numbers
        for length in range(min_len, max_len + 1):
            # Slide a window of 'length' over the sample string
            for start in range(10 - length):
                substring = sample[start : start + length]
                num = int(substring)
                
                # If the number fits in our target range, collect it
                if low <= num <= high:
                    result.append(num)
                    
        return result