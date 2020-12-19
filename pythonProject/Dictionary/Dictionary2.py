# Dictionary Comprehension
squares = {x: x*x for x in range(6)}

print(squares)


squares ={}
for x in range(6):
    squares[x] = x*x
print(squares)


# Dictionary Comprehension with if conditional
odd_squares = {x: x*x for x in range(11) if x % 2 == 1}

print(odd_squares)

# Iterating through a Dictionary
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(squares[i])

