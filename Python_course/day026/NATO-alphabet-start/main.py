import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    user_word = input("Enter a word: ").upper()
    try:
        nato_alphabet = [data_dict[value] for value in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet, please")
        generate_phonetic()
    else:
        print(nato_alphabet)


generate_phonetic()
