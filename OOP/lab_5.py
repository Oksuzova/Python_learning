# Oksuzova T. io-z21
nzk = 2108

import string

class Letter:

    def __init__(self, symbol):
        self.symbol = symbol

    def set_value(self, symbol):
        self.symbol = symbol

    def get_value(self):
        return self.symbol

    def __eq__(self, other):
        return isinstance(other, Letter) and self.symbol == other.symbol

    def __hash__(self):
        return hash(self.symbol)

    def __str__(self):
        return self.symbol

class Punctuation:

    def __init__(self, symbol):
        self.symbol = symbol

    def __eq__(self, other):
        return isinstance(other, Letter) and self.symbol == other.symbol

    def __hash__(self):
        return hash(self.symbol)

    def __str__(self):
        return self.symbol

class Word:

    def __init__(self, word):
        self.word = word
        self.letters = [Letter(x) if x not in string.punctuation else Punctuation(x) for x in word]

    def get_value(self):
        return self.letters

    def __iter__(self):
        return iter(self.letters)

    def __eq__(self, other):
        return isinstance(other, Word) and self.letters == other.letters

    def __hash__(self):
        return hash(tuple(self.letters))

    def __str__(self):
        return ''.join(map(str, self.letters))

class Sentence:
    def __init__(self, sentences):
        self.word_mass = []
        self.sentences = [Word(x) for x in sentences.split()]

    def get_value(self):
        return self.word_mass

    def __iter__(self):
        return iter(self.sentences)

    def __eq__(self, other):
        return isinstance(other, Sentence) and self.sentences == other.sentences

    def __hash__(self):
        return hash(tuple(self.sentences))

    def __str__(self):
        sentence_string = "" + str(self.sentences[0])
        for index in range(1, len(self.sentences)):
            if isinstance(self.sentences[index], Word):
                sentence_string += ' ' + str(self.sentences[index])
            else:
                sentence_string += '' + str(self.sentences[index])
        return sentence_string

class Text:
    def __init__(self, text):
        self.text = text
        self.sentences = []
        self.set_value()

    def get_value(self):
        return self.sentences

    def set_value(self):
        new_txt = self.text.strip()
        self.sentences = [Sentence(x) for x in new_txt.lower().split(".")]

    def __iter__(self):
        return iter(self.sentences)

    def __str__(self):
        return ''.join(map(str, self.sentences))

def main():
    text = Text("Also distorting our sense of danger is our moral psychology." 
        "No one has ever recruited activists to a cause by announcing that things are getting better, " 
        "and bearers of good news are often advised to keep their mouths shut lest " 
        "they lull people into complacency." 
        "Also, a large swath of our intellectual culture is loath to admit that there could be anything " 
        "good about civilization, modernity, and Western society. But perhaps the main cause" 
        " of the illusion of ever-present violence springs from one of the forces that drove violence down" 
        " in the first place. The decline of violent behavior has been paralleled by a decline in" 
        " attitudes that tolerate or glorify violence, and often the attitudes are in the lead." 
        "By the standards of the mass atrocities of human history, the lethal " 
        "injection of a murderer in Texas, " 
        "or an occasional hate crime in which a member of an ethnic minority is intimidated by hooligans, " 
        "is pretty mild stuff. But from a contemporary vantage point, " 
        "we see them as signs of how low our behavior can sink, not of how high our standards have risen.")



    unique_list = []
    for sentences in text.sentences:
        for word in sentences:
            if word not in unique_list:
                unique_list.append(word)

    num = 0
    count = {word: num for word in unique_list}
    for key in count:
        for sentences in text.sentences:
            if key in sentences:
                count[key] += 1
    max_val = max(count.values())
    result_k = {v: k for k, v in count.items() if v == max_val}
    print(f"The word '{result_k[max_val]}' occurs in {max_val} sentences of the given text.")


if __name__ == '__main__':
    main()
