from model.IMarcowChain import IMarcowChain
from model.FirstOrderMarcowChain import FirstOrderMarcowChain

class MarcowChainFactory():
    def first_order(self) -> IMarcowChain:
        return FirstOrderMarcowChain()
