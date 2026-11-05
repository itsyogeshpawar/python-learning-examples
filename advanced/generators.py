# Generators in Python
# Functions that yield values one at a time.

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(5):
    print(num)

# Explanation:
# - Use 'yield' to make a generator function.
# - Generators are memory efficient for large data.
