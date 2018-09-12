x = input("Type a sentence")
y = x.split()
for word in y:
    z = list(word)
    for letter in z:
        print(letter)
    print("-")
