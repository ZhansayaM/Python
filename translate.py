def translate(word):
    new = ""
    for x in word:
        if x.lower() in "aeiou":
            if x.isupper():
                new = new + "Z"
            else:
                new = new + "z"
        else:
            new = new + x
    return new

print(translate(input("Please, enter a word to translate: ")))
