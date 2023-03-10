import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

user_word = input("Enter a word: ").upper()

nato_alphabet = [data_dict[value] for value in user_word]

print(nato_alphabet)
