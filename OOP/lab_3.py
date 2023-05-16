# Oksuzova T. io-z21

class First:
    def __init__(self):
        self.nzk = 2108
        self.c3 = self.nzk % 3      # 2 String
        self.c13 = self.nzk % 17    # 0 Find the largest number of sentences of the given text that contain the same words.

        self.text = "Also distorting our sense of danger is our moral psychology." \
                    "No one has ever recruited activists to a cause by announcing that things are getting better, " \
                    "and bearers of good news are often advised to keep their mouths shut lest " \
                    "they lull people into complacency." \
                    "Also, a large swath of our intellectual culture is loath to admit that there could be anything " \
                    "good about civilization, modernity, and Western society. But perhaps the main cause" \
                    " of the illusion of ever-present violence springs from one of the forces that drove violence down"\
                    " in the first place. The decline of violent behavior has been paralleled by a decline in" \
                    " attitudes that tolerate or glorify violence, and often the attitudes are in the lead." \
                    "By the standards of the mass atrocities of human history, the lethal " \
                    "injection of a murderer in Texas, " \
                    "or an occasional hate crime in which a member of an ethnic minority is intimidated by hooligans, "\
                    "is pretty mild stuff. But from a contemporary vantage point, " \
                    "we see them as signs of how low our behavior can sink, not of how high our standards have risen."

    def find(self):
        new_txt = self.text.strip()
        list_of_sentences = new_txt.lower().split(".")
        self.words_list(list_of_sentences)

    def words_list(self, list_sents: list):
        words_list = []
        for line in list_sents:
            new_line = line.replace(",", "").strip().split(" ")
            words_list.append(new_line)
        self.unique_word(words_list)

    def unique_word(self, words: list):
        unique_word = []
        for line in words:
            for word in line:
                if word not in unique_word:
                    unique_word.append(word)
        self.executive_method(words, unique_word)

    def executive_method(self, words: list, unique_list: list):
        num = 0
        count = {word: num for word in unique_list}
        for word in count:
            for line in words:
                if word in line:
                    count[word] += 1
        max_val = max(count.values())
        result_k = {v: k for k, v in count.items() if v == max_val}
        print(f"The word '{result_k[max_val]}' occurs in {max_val} sentences of the given text.")

def main():
    first = First()
    first.find()


if __name__ == '__main__':
    main()



