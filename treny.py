from TextGenerator import TextGenerator
import re

lines = re.split('\\.|\\!|\\?', open('texts/treny.txt', encoding='utf8').read())

for i in range(len(lines)):
    lines[i] += '.'

generator = TextGenerator(lines)
print(generator.generate_line())
