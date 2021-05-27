cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# to maintain original order of a list but present in a sorted order, use sorted() function
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))

