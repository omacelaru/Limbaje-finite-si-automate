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
        self.MAX = str(int(max(list({x[1] for x in input_text}))) + 1) # maximul pt lambda
        self.alfabet = sorted(list({x[1] if int(x[1]) != -1 else self.MAX for x in input_text }))

        # formarea functiei delta
        self.matrix = [[-1 for x in range(len(self.alfabet))] for y in range(len(self.states))]

        for line in input_text:
            i = self.states.index(line[0])
            j = self.alfabet.index(line[1] if int(line[1]) != -1 else self.MAX)
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
                if self.matrix[i][-1] != -1:
                    for k in self.matrix[i][-1]:
                        if k in self.start:
                            break
                    else:
                        self.start.extend(self.matrix[i][-1])
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
        for v in self.alfabet[:-1]:
            self.s[k] = v
            if k == self.N - 1:
                self.words.append("".join(self.s))
            else:
                self.bkt(k+1)

file = 5
file_name = "input" + str(file) + ".in"

n = 5

# cazul cu lungime 0
result = []
graph = GRAPH(file_name,n)
print("Lungime maxima: 0", )
print()
if graph.start_node in graph.final_nodes:
    result.append("")
    ok = 1
    print(1)
else:
    ok = 0
    print(0)
print()
del graph


for N in range(1,n+1):
    print("Lungime maxima: ", N)
    graph = GRAPH(file_name,N)
    graph.bkt(0)

    if ok == 1:
        result = result[:1]
    else:
        result = []
    for word in graph.words:
        if graph.verify_word(word) == True:
            word = word.replace(graph.MAX,'\u03BB')
            result.append(word)

    print(*result, sep="\n")
    print(len(result))
    print()
    del graph

