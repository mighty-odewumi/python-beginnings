def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "I"
            else:
                translation = translation + "i"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase and check out this cool translator: ")))



















