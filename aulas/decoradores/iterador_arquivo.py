import os

class FileIterator:
    def __init__(self, filename) -> None:
        self.file = open(filename)

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if line != '':
            return line
        else:
            self.file.close()
            raise StopIteration


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'text_example.txt')

for line in FileIterator(filename):
    print(line)
