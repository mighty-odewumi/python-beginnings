#Tutorial on None
def some_func():
    print("Hi!")
#some_func()

var = some_func()
print(var)

#Tutorial on Dictionaries
#try:

coffee_drinking_per_person_per_cups = {"Europe" : 750, "U.S." : 400, "Japan/South Korea" : 200, "China" : 4 }
print(coffee_drinking_per_person_per_cups["Japan/South Korea"])
print(coffee_drinking_per_person_per_cups)
#except KeyError as err:
#    print(err)
print(coffee_drinking_per_person_per_cups["China"])

squares = {1 : 1, 2 : 2, 3 : "error", 4 : 16}
squares[3] = 9
squares[8] = 64
print(squares)
print(1 in squares)
print("error" in squares)
print(16 in squares)
print(squares.get(5, "Key not found"))

try:
    words = ("spam", "eggs", (1,2,3,4), (4,5), "juice",)
    print(words[2][2]) #Outputs the third element in the third tuple(nested).
    words[1] = "hamburger" #Tuple objects are immutable.
    print(words)
except TypeError as error:
    print(error)

words = ["spam", "eggs", (1,2,3,4), (4,5), "juice", 2, 3, 4, 5]

print(words[2:])
print(words[::-1]) #Reverses the list i.e. it is another way to reverse the list.
print(words[2:8:3])
print(words[::2])

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[7:5:-1]) # A sololearn exercise but it is unclear to me.

evens = [i ** 2 for i in range(10) if i ** 2 % 2 == 0]
print(evens) #Prints even numbers from 0 to 64 which are in the range of 10
# and are divisible by 2

multiples = [i for i in range(1, 20) if i % 3 == 0]
print(multiples)
# Prints multiples of 3 ranging from 1 to 20

"""
try:
    even = [2*i for i in range(10**100)]
    print(even)
except MemoryError as err:
    print(err)
"""

nums = [4,5,6]
msg = "Numbers: {0} {1} {2}" .format(nums[0], nums[1], nums[2],)
print(msg)

a = "{x}, {y}" . format(x = 5, y = 12)
print(a)

# String functions
print("This is a sentence.".replace("sentence", "paragraph"))
print("This is a sentence.".startswith("This"))
print("This is a sentence.".split(","))
print("This is a sentence.".lower())
print("This is a sentence.".upper())
print("This is a sentence.".endswith("sentence"))
print(",".join(["eggs", "hamburger", "cheese"]))

# Numeric functions
print(min([1,2,3,4,5,6,7]))
print(max([1,2,3,4,5,6]))
print(abs(-99))
print(abs(42))
print(round(59))
print(sum([1,2,3,4,5,6]))

# List functions
nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
    print("All are greater than 5.")

if any([i % 2 == 0 for i in nums]):
    print("At least one is even")

for v in enumerate(nums):
    print(v)


nums = [-1, 2, -3, 4, -5]
if all([abs(i) < 3 for i in nums]):
    print(1)
else:
    print(2)
# Prints 2


# Text analyzer
filename = input("Enter a filename: ")
with open(filename) as f:
    text = f.read()
print(text)


def count_char(text, char):
    count = 0
    for h in text:
        if h == char:
            count += 1
    return count

filename = input("Enter a filename: ")
with open(filename) as f:
    text = f.read()

for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * count_char(text, char) / len(text)
    print("{0} - {1}%" . format(char, round(perc, 2)))


print(count_char(text, "e"))

def polynomial(x):
    return x ** 2 + 2 * x + 4
print(polynomial(2))

#Using lambdas
print((lambda x: x ** 2 + 2 * x + 4)(2))

#Use of the map functions
def add_five(x):
    return x + 5
nums = [11, 22, 33, 44, 55]
result = list(map(add_five , nums))
print(result)

nums = [11, 22, 33, 44, 55]
result  = list(map(lambda x : x + 5, nums))
print(result)



