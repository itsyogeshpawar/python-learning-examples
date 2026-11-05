# File I/O in Python
# Reading from and writing to files.

# Writing to a file
with open("example.txt", "w") as f:
    f.write("Hello, file!\n")

# Reading from a file
with open("example.txt", "r") as f:
    content = f.read()
    print(content)

# Explanation:
# - Use open() with 'w' to write and 'r' to read.
# - with ensures the file is properly closed.
