import string


def encrypt(text, shift, direction):
    entext = list()
    if direction == "decode":
        shift *= -1
    for letter in text:
        if letter in string.ascii_lowercase:
            position = string.ascii_lowercase.index(letter)
            new_position = (position + shift) % 26
            new_letter = string.ascii_lowercase[new_position]
        else:
            new_letter = letter
        entext.append(new_letter)
    entext = "".join(entext)
    result = open('text.txt', 'w')
    result.write(entext)
    result.close()


choice = False
while not choice:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    text = open("text.txt", "r")
    text = text.read()

    shift = int(input("Type the shift number:\n"))

    encrypt(text, shift, direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        choice = True
        print("Goodbye!")
