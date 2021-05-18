bicycles = ['trek', 'cannondale', 'schwinn', 'redline', 'specialized', 'mongoose']
cars = ['ford', 'chevrolet', 'toyota', 'honda', 'mini', 'jeep']
print(bicycles)
print(bicycles[0]) # you can access any element in a list by telling Python the position, or INDEX, of the item. Note that indexes start at 0, not one.
print(bicycles[0].title()) # better formatting
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1]) #-1 will always return the last item in the list.

message = f"My first bicycle was a {bicycles[1].title()}. My first car was a {cars[5].title()}."
print(message)