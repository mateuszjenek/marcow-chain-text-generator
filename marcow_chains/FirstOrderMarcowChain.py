import numpy

from marcow_chains.IMarcowChain import IMarcowChain

class FirstOrderMarcowChain(IMarcowChain):

    def __init__(self):
        self.word_dict = {}
    
    def feed(self, lines: [str]):
        for line in lines:
            self.__add_line_to_dict(line)

    def generate(self) -> str:
        first_word = numpy.random.choice(self.word_dict[""])
        chain = [first_word]
        while True:
            if not chain[-1] in self.word_dict.keys():
                break
            next_word = numpy.random.choice(self.word_dict[chain[-1]])
            chain.append(next_word)
            if next_word == "":
                break
        return ' '.join(chain)

    def __add_line_to_dict(self, line):
        pairs = self.__make_pairs(line.split())
        for word_1, word_2 in pairs:
            if word_1 in self.word_dict.keys():
                self.word_dict[word_1].append(word_2)
            else:
                self.word_dict[word_1] = [word_2]

    def __make_pairs(self, words):
        yield ("", words[0])
        for i in range(len(words)-1):
            yield (words[i], words[i+1])
        yield (words[-1], "")
