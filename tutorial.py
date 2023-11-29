friends = ["Pelumi", "Elisha", "Taiwo", "Kehinde", "Samuel", "Teslim"]
print(friends)

friends = ["Pelumi", "Elisha", "Taiwo", "Kehinde", "Samuel", "Teslim"]
friends2 = friends.copy()
print(friends2)
friends2.sort()
print(friends2)
friends2.reverse()

friends2.append("Reece")
print(friends2)

print(friends2.pop())
print(friends.pop())

print(friends2.pop())
print(friends2)
print(friends.pop())
print(friends)


coordinates =  [(4,5),(2,4), (3,5),(289,89)] #this is a tuple in a list
#tuples are enclosed by parentheses and are immutable i.e. they are cannot be changed.
(coordinates.insert(1, (58,38)))
print(coordinates)

