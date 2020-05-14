from model.MarcowChainFactory import MarcowChainFactory
from model.IMarcowChain import IMarcowChain

class ViewModel():
    marcow_factory = MarcowChainFactory()

    def __init__(self):
        self.sources = []
        self.generated_text = ""
        self.__generator = self.marcow_factory.first_order()
    
    def add_source(self, file_path: str):
        self.sources.append(file_path)
        lines = open(file_path, encoding='utf8').read().splitlines()
        self.__generator.feed(lines)

    def reset_sources(self):
        self.sources = []
        self.__generator.reset()

    def generate_sentence(self) -> str:
        return self.__generator.generate()
        