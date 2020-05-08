from TextGenerator import TextGenerator

lines = open('texts/treny.txt', encoding='utf8').read().rstrip().split('.')
for i in range(len(lines)):
    lines[i] += '.'

generator = TextGenerator(lines)
print(generator.generate_line())
