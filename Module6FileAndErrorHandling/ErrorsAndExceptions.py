# print("Hello")
# print("world")

def div(a, b):
    try :
        print(a / b)
    except :
        pass
    
    print("Hello")


# try :
#     a = int('Aniket')
#     print(10 / 0)
# except ZeroDivisionError:
#     print("You were trying to divide by 0")
# except ValueError:
#     print("Trying to convert string to int")

# try:
#     print(10 /0)
# except Exception as e:
#     print(type(e))

# try :
#     raise Exception("My Custum Error", 1, 2)
# except Exception as e:
#     print(e)

class MyException(Exception):
    def __init__(self, message) -> None:
        self.message = message
    def __str__(self) -> str:
        return self.message


# try:
#     raise MyException('some error')
# except Exception as e:
#     print(e)

# else : will always execute if the try block didn't threw any error
# finally : will always execute

try :
    print("Hello World")
    print(10 / 0)
except :
    print("Ok Error Occured")
else :
    print("Woah")
finally :
    # Cleanup Code
    print("Bye Bye World")

# with open("something.txt", "r") as file:
#     print(file.read())

class A:
    def __init__(self, n) -> None:
        self.n = n
    def __str__(self) -> str:
        return str(self.n)
    
    def __enter__(self):
        return self
    def __exit__(self, *args):
        print(args)
        return True # Not want to raise any error
        return False # Raise the error

with A(5) as a:
    print(a)
    raise 10/0
print("hello")
