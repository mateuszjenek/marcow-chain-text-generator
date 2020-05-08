from TextGenerator import TextGenerator

lines = open('texts/motivate lines.txt', encoding='utf8').read().splitlines()

generator = TextGenerator(lines)
print(generator.generate_line())
