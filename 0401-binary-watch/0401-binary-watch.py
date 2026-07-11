class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        res = []
        
        # Loop through every possible hour (0-11) and minute (0-59)
        for h in range(12):
            for m in range(60):
                # Count total set bits (1s) in the binary representation of h and m
                if h.bit_count() + m.bit_count() == turnedOn:
                    # Format minutes to always have two digits (e.g., 3 -> "03")
                    res.append(f"{h}:{m:02d}")
                    
        return res    