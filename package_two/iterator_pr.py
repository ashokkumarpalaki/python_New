class Counter(object):
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        'Returns itself as an iterator object'
        return self

    def __next__(self):
        'Returns the next value till current is lower than high'
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

    def counter_generator(self, low, high):
        while low <= high:
            yield low
            low += 1


if __name__ == '__main__':
    count = Counter(1, 6)
    print(count.__next__())
    print(count.counter_generator(1, 3).__next__())
