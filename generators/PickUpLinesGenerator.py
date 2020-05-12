from generators.ITextGenerator import ITextGenerator
from marcow_chains.IMarcowChain import IMarcowChain

class PickUpLinesGenerator(ITextGenerator):
    def __init__(self, marcow_chain: IMarcowChain):
        self.marcow_chain = marcow_chain
        lines = open('texts/pick-up_lines.txt', encoding='utf8').read().splitlines()
        marcow_chain.feed(lines)

    def generate(self) -> str:
        return self.marcow_chain.generate()
