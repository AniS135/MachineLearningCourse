# Read Only ('r') # Default Raise error if file doesn't available
# Read and Write('r+')
# Write Only ('w') Open and remove all data from file and start writing
# Write and Read ('w+')
# Append Only ('a') Append(don't remove data)
# Append and Read ('a+')

# # Openning a file

# file = open("hello.txt", "r")
# print(file.read(5))

# # Closing a file
# file.close()

# file = open('something.txt', 'w')
# file.write("Hello from other side")

# file.close()

# file = open('hello.txt')
# print(file.readlines())

# file.close()

# file = open('hello.txt', 'r')

# print(file.read(5))
# print(file.read())

# file.seek(0)

# print(file.read())

# file.close()


# Smarter way to open file as it itself close file and open can be only performed in specific block
with open('hello.txt', 'r') as file:
    print(file.read())
    file.seek(4)
    print(file.read())



