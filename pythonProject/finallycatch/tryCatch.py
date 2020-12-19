try:
    k = 5 // 0  # raises divide by zero exception.
    print(k)

# handles zerodivision exception
except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')

try:
    k = 5 // 1  # No exception raised
    print(k)

# intends to handle zerodivision exception
except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')

# Python program to demonstrate finally

# Exception is not handled
try:
    k = 5 // 0  # exception raised
    print(k)

finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')