x = [1, 2, 3]

x_iter = iter(x)

# It is both iterable and iterator
class yrange:
#      n is the number upto which I want the range
    def __init__(self, n) -> None:
        self.i = 0
        self.n = n
#      This method makes our class iterable
    def __iter__(self):
        return self
#      This method should be implemented by the ITERATOR
    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

# for x in yrange(5):
#     print(x)

y = yrange(5)

print("When we make both iterable and iterator in a class")
print(list(y))
print(list(y))


# y = yrange(5)

# y_iter = iter(y)

# This is iterable
class zrange:
    def __init__(self, n) -> None:
        self.n = n

    def __iter__ (self):
        return zrange_iter(self.n)


# This is iterator
class zrange_iter:
    def __init__(self, n) -> None:
        self.i = 0
        self.n = n
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

# for x in zrange(5):
#     print(x ** 2)

z = zrange(5)

print("When we make both iterator and iterable prop in diff class")

print(list(z))
print(list(z))



