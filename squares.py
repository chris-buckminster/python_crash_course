squares = []
for value in range(1,21):
	square = value ** 2
	squares.append(square)

print(squares)

squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)

digits = [1, 2, 33, 4, 52, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value**2 for value in range(1, 11)] #this is called a list comprehension. you can generate the same list in one line of code.
print(squares)