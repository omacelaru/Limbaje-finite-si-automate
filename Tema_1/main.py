def read_data(name_file="input1.in"):
    input = []
    with open(name_file) as f:
        init = f.readline().strip().lower() # starea initiala
        final = f.readline().strip().lower().split()  # starea finala
        for line in f:
            input.append(line.strip().lower().split())

    input.sort(key=lambda t: (t[:][0], t[:][1]))  # sortarea datelor

    # extragerea unica a starilor
    stari = {x[0] for x in input}
    stari_second = {x[2] for x in input}
    stari = stari.union(stari_second)
    stari = list(stari)
    stari.sort()

    # extagerea unica a alfabetului
    alfabet = {x[1] for x in input}
    alfabet = list(alfabet)
    alfabet.sort()

    # formarea functiei delta
    matrix = [[0 for x in range(len(alfabet))] for y in range(len(stari))]
    for line in input:
        i = int(line[0][-1])
        j = int(line[1]) if line[1].isdigit() else ord(line[1]) - ord('a')
        matrix[i][j] = line[2]
    return stari, alfabet, matrix, init, final


def verify_word(cuv, matrix, init, final):
    path = []
    for c in cuv:
        path.append(init)                                  # adaugarea componentei in drum

        i = int(init[-1])                                  #
        j = int(c) if c.isdigit() else ord(c) - ord('a')   # parcurgerea functiei delta
        init = matrix[i][j]                                #
        if init == 0:                                      # verificarea unei erori de citire a datelor
            print("Input gresit")
            return False, []

    path.append(init)                                      # adaugarea ultimei stari in drum

    if init in final:
        return True, path
    return False, []

name_file_input = "input2.in"
name_file_test = "test2.in"

stari, alfabet, matrix, init, final = read_data(name_file_input)

with open(name_file_test) as f:
    # citirea cuvintelor penrtu test
    words = []
    for line in f:
        words.append(line.strip().lower())

for word in words:
    print("Cuvantul testat este: ", word)

    is_accepted, path = verify_word(word, matrix, init, final)

    if is_accepted == True:
        print("Acceptat")
        sir = " -> ".join(path)
        print(sir)
    else:
        print("RESPINS")
    print()
