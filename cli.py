import argparse
from model.IMarcowChain import IMarcowChain
from model.MarcowChainFactory import MarcowChainFactory

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-s", "--source", required=True, help="Text file with line-by-line sentences")
args = arg_parser.parse_args()

lines = open(args.source, encoding='utf8').read().splitlines()
               
generator = MarcowChainFactory().first_order()
generator.feed(lines)
print(generator.generate())
