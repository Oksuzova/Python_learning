def encrypt(text, shift, direction):
    entext = ""
    if direction == "decode":
        shift *= -1
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        if direction == "encode" and new_position > 25:
            new_position = new_position - 26
        if direction == "decode" and new_position < 0:
            new_position = new_position + 26
        new_letter = alphabet[new_position]
        entext += new_letter
    print(entext)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

encrypt(text, shift, direction)
