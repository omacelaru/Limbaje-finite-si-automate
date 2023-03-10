class graph:
    def __init__(self, name_file="input1.in"):
        input_text = []
        with open(name_file) as f:
            self.start_node = f.readline().strip().lower()  # starea initiala
            self.final_nodes = f.readline().strip().lower().split()  # stari finale
            for line in f:
                input_text.append(line.strip().lower().split())
        input_text.sort(key=lambda t: (t[:][0], t[:][1]))  # sortarea datelor

        # extragerea unica a starilor
        self.states = sorted(list(set([s[0] for s in input_text]) | set([s[2] for s in input_text])))

        # extagerea unica a alfabetului
        self.alfabet = sorted(list({x[1] for x in input_text}))

        # formarea functiei delta
        self.matrix = [[0 for x in range(len(self.alfabet))] for y in range(len(self.states))]
        for line in input_text:
            i = int(line[0][-1])
            j = int(line[1]) if line[1].isdigit() else ord(line[1]) - ord('a')
            self.matrix[i][j] = line[2]

    def verify_word(self, word):
        path = []
        for c in word:
            path.append(self.start_node)  # adaugarea componentei in drum

            i = int(self.start_node[-1])  #
            j = int(c) if c.isdigit() else ord(c) - ord('a')  # parcurgerea functiei delta
            self.start_node = self.matrix[i][j]  #
            if self.start_node == 0:  # verificarea unei erori de citire a datelor
                print("Input gresit")
                return False, []

        path.append(self.start_node)  # adaugarea ultimei stari in drum

        if self.start_node in self.final_nodes:
            return True, path
        return False, []

name_file_input = "input2.in"
name_file_test = "test2.in"

graph = graph(name_file_input)

with open(name_file_test) as f:
    # citirea cuvintelor penrtu test
    words = []
    for line in f:
        words.append(line.strip().lower())

for word in words:
    print("Cuvantul testat este: ", word)

    is_accepted, path = graph.verify_word(word)

    if is_accepted == True:
        print("Acceptat")
        sir = " -> ".join(path)
        print(sir)
    else:
        print("RESPINS")
    print()
