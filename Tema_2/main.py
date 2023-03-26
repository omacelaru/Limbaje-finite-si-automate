class GRAPH:
    def __init__(self, name_file,n):
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
        self.matrix = [[-1 for x in range(len(self.alfabet))] for y in range(len(self.states))]

        for line in input_text:
            i = self.states.index(line[0])
            j = self.alfabet.index(line[1])
            if self.matrix[i][j] == -1:
                self.matrix[i][j] = [line[2]]
            else:
                self.matrix[i][j].append(line[2])
        self.s = [''for _ in range(n)]
        self.N = n


    def verify_word(self, word):
        self.start = [self.start_node]
        for c in word:

            j = self.alfabet.index(c) # parcurgerea functiei delta
            next = []
            for x in self.start:
                i = self.states.index(x)
                if x == -1:  # verificarea unei erori de citire a datelor
                    print("Input gresit")
                    return False
                # print(self.start,i,j,c, self.matrix[i][j])
                if self.matrix[i][j] != -1:
                    next.extend(self.matrix[i][j])
            self.start = next

        for node in self.start:
            if node in self.final_nodes:
                return True
        return False

    words = []
    def bkt(self,k):
        for v in self.alfabet:
            self.s[k] = v
            if k == self.N - 1:
                self.words.append("".join(self.s))
            else:
                self.bkt(k+1)

file = 3
file_name = "input" + str(file) + ".in"

n = 100
graph = GRAPH(file_name,n)
graph.bkt(0)

result = []
for word in graph.words:
    if graph.verify_word(word) == True:
        result.append(word)

print(*result, sep="\n")
print(len(result))

