import argparse

from model.FirstOrderMarcowChain import FirstOrderMarcowChain

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-s", "--source", required=True, help="Text file with line-by-line sentences")
args = arg_parser.parse_args()

lines = open(args.source, encoding='utf8').read().splitlines()
               
generator = FirstOrderMarcowChain()
generator.feed(lines)
print(generator.generate())
