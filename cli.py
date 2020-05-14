import argparse
from marcow_chain.FirstOrderMarcowChain import FirstOrderMarcowChain
from generator.TextGenerator import TextGenerator

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-s", "--source", required=True, help="Text file with line-by-line sentences")
args = arg_parser.parse_args()

generator = TextGenerator(FirstOrderMarcowChain(), args.source)

print(generator.generate())
