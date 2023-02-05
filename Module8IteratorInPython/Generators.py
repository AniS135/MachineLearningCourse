class fib:
    def __init__(self) -> None:
        self.prev = 0
        self.curr = 1

    def __iter__(self) :
        return self

    def __next__ (self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value

f = iter(fib())

# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))

# genrator function
def fib():
    prev, curr = 0, 1
    while True :
        yield curr
        prev, curr = curr, prev + curr

gen = (x ** 2 for x in range(1, 11))

a = gen