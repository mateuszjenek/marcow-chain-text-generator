import numpy

class TextGenerator:
    word_dict = {}
    
    def __init__(self, texts):
        self.feed(texts)
    
    def __make_pairs(self, words):
        yield ("", words[0])
        for i in range(len(words)-1):
            yield (words[i], words[i+1])
        yield (words[-1], "")

    def __add_text_to_dict(self, text):
        pairs = self.__make_pairs(text.split())
        for word_1, word_2 in pairs:
            if word_1 in self.word_dict.keys():
                self.word_dict[word_1].append(word_2)
            else:
                self.word_dict[word_1] = [word_2]

    def feed(self, texts):
        for text in texts:
            self.__add_text_to_dict(text)

    def generate_line(self):
        first_word = numpy.random.choice(self.word_dict[""])
        return self.generete_line_starting_with(first_word)

    def generete_line_starting_with(self, word):
        if not word in self.word_dict.keys():
            return ""
        chain = [word]
        while True:
            if not chain[-1] in self.word_dict.keys():
                break
            next_word = numpy.random.choice(self.word_dict[chain[-1]])
            chain.append(next_word)
            if next_word == "":
                break
        return ' '.join(chain)
