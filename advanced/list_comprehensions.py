# List Comprehensions in Python
# Concise way to create lists.

squares = [x * x for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# With condition
even_squares = [x * x for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]

# Explanation:
# - [expression for item in iterable] creates a new list.
# - You can add conditions with 'if'.
