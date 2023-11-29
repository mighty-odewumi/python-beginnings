def say_hi(name, age):
    print("Hello " + name + ", you are " + str(age) + " years old.")


say_hi("Mighty", '16')
say_hi("Sam", "17")


def cube_num(number):
    return number * number * number


result = cube_num(3)
print(result)


is_male = False
is_tall = False


if is_male and is_tall:
    print("You are a male and are tall.")
elif is_male and not is_tall:
    print("You are not tall but a male.")
elif not is_male and is_tall:
    print("You are not a male but are tall.")
else:
    print("You are not a male and are not tall.")


def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(2,41,468))