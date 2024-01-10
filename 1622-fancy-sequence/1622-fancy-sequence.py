class Fancy:
    def __init__(self):
        self.MOD = 10**9 + 7
        self.appended = []
        self.add_factor = 0
        self.mul_factor = 1

    def append(self, val: int) -> None:
        # Adjust the value based on current factors before appending
        val = (val - self.add_factor) * pow(self.mul_factor, self.MOD - 2, self.MOD)
        self.appended.append(val)

    def addAll(self, inc: int) -> None:
        # Update the add factor
        self.add_factor = (self.add_factor + inc) % self.MOD

    def multAll(self, m: int) -> None:
        # Update both factors
        self.mul_factor = (self.mul_factor * m) % self.MOD
        self.add_factor = (self.add_factor * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.appended):
            return -1
        # Apply the factors to the element at idx
        val = self.appended[idx]
        val = (val * self.mul_factor + self.add_factor) % self.MOD
        return val
