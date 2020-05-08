from TextGenerator import TextGenerator

lines = open('texts/pick-up lines.txt', encoding='utf8').read().splitlines()

generator = TextGenerator(lines)
print(generator.generate_line())
