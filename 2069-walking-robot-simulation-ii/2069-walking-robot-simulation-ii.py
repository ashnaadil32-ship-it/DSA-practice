class Robot:
    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        # Total distinct positions along the perimeter loop
        self.perimeter = 2 * (width + height) - 4
        self.pos_idx = 0
        self.moved = False

    def step(self, num: int) -> None:
        self.moved = True
        # Reduce unnecessary full boundary laps
        self.pos_idx = (self.pos_idx + num) % self.perimeter

    def getPos(self) -> list[int]:
        idx = self.pos_idx
        
        # Bottom row: moving East
        if idx < self.w:
            return [idx, 0]
        # Right column: moving North
        if idx < self.w + self.h - 1:
            return [self.w - 1, idx - (self.w - 1)]
        # Top row: moving West
        if idx < 2 * self.w + self.h - 2:
            return [self.w - 1 - (idx - (self.w + self.h - 2)), self.h - 1]
        # Left column: moving South
        return [0, self.h - 1 - (idx - (2 * self.w + self.h - 3))]

    def getDir(self) -> str:
        # Edge Case: Robot hasn't moved yet
        if not self.moved or self.pos_idx == 0:
            return "East" if not self.moved else "South"
            
        idx = self.pos_idx
        # Determine the direction based on segment ranges
        if 0 < idx < self.w:
            return "East"
        if self.w <= idx < self.w + self.h - 1:
            return "North"
        if self.w + self.h - 1 <= idx < 2 * self.w + self.h - 2:
            return "West"
        return "South"