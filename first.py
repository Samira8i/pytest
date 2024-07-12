class Number:
    def __init__(self, numbers):
        self.numbers = numbers

    def sum(self):
        return sum(self.numbers)

    def sr(self):
        return sum(self.numbers) / len(self.numbers)

    def max(self):
        return max(self.numbers)

    def min(self):
        return min(self.numbers)

