import string
import time
def encrypt(text, shift, direction):
    start = time.time()
    entext = list()
    if direction == "decode":
        shift *= -1
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift) % 26
            new_letter = alphabet[new_position]
        else:
            new_letter = letter
        entext.append(new_letter)
    entext = "".join(entext)
    result = open('text.txt', 'w')
    result.write(entext)
    result.close()
    end = time.time()
    print(end)


alphabet = list(string.ascii_lowercase)                              #add the list of alphabet letters

choice = False
while not choice:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    doc = open("text.txt")
    text = list()
    for line in doc:
        line = line.rstrip()
        text.append(line)
    text = "".join(text)
    shift = int(input("Type the shift number:\n"))

    encrypt(text, shift, direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        choice = True
        print("Goodbye!")
