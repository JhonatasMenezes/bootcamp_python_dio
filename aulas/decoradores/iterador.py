class MeuIterador:
    def __init__(self, numbers: list[int]) -> None:
        self.numbers = numbers
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            number = self.numbers[self.counter]
            self.counter += 1
            return number * 2
        except IndexError:
            raise StopIteration

for i in MeuIterador([1, 2, 3, 4, 5, 6, 7, 8]):
    print(i)
