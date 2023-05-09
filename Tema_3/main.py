def citire(intput_file_gramatica, input_file_cuvinte):
    gramatica = {}
    with open(intput_file_gramatica) as f:
        for line in f:
            line = line.strip().split(" -> ")
            key = line[0]
            value = line[1].split(" | ")
            if "-1" in value:
                value[value.index("-1")] = ""
            value.sort(key=lambda t: (-len(t)) )
            if key not in gramatica:
                gramatica[key] = value
            else:
                gramatica[key].extend(value)

    words = []
    with open(input_file_cuvinte) as f:
        for line in f:
            words.append(line.strip())
    return gramatica, words


def derive_word(word, productions, symbol):
    if word == "":
        if symbol.isupper():
            return '' in productions[symbol]
        else:
            return True;

    if symbol in productions:
        for production in productions[symbol]:
            if production == "":
                if derive_word(word, productions, symbol[1:]):
                    return True
            elif production[0] == word[0]:
                if derive_word(word[1:], productions, production[1:]):
                    return True
    return False
def verify_words(grammar, word_list):
    g = open("output.txt", "w")
    for word in word_list:
        if derive_word(word, grammar, "S"):
            print(f"Cuvântul '{word}' aparține limbajului generat de gramatică.\n")
            g.write(f"Cuvântul '{word}' aparține limbajului generat de gramatică.\n")
        else:
            # print(f"Cuvântul '{word}' nu apartine\n")
            g.write(f"Cuvântul '{word}' nu apartine\n")
    g.close()

file = 1
input_file_gramatica = "input" + str(file) + "gramatica.in"
input_file_cuvinte = "input" + str(file) + "cuvinte.in"
gramatica, words = citire(input_file_gramatica, input_file_cuvinte)

verify_words(gramatica, words)
