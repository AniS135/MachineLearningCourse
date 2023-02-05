# Different Ways to achieve astnchronous programming in python
# 1. Multi Processing
# 2. Multi Threading
# 3. Couroutines
# 4. AsyncIO # lib present from 3.7 + version

def func2():
    return 5

def func():
    yield func2()

def main():
    pass
