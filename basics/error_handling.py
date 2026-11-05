# Error Handling in Python
# Handling exceptions with try/except.

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This always runs.")

# Explanation:
# - try/except handles errors gracefully.
# - finally block always executes.
