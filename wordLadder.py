import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra, connected_components


class WordLadder:

    def __init__(self):
        self.graph = None
        self.word_list = None
        self.start = None
        self.end   = None

    def cleanUP(self):
        wordlist = open("data/words.txt").readlines() ### Reading the Dicitionary
        wordlist = map(str.strip, wordlist)  ###
        wordlist = [word for word in wordlist if len(word) == 3 and word[0].islower() and word.isalpha()]
        wordlist = list(map(str.lower, wordlist))

        self.word_list = np.asarray(wordlist)
        self.word_list.word_list.sort()


        word_bytes = np.ndarray((self.word_list.size, self.word_list.itemsize), dtype='uint8', buffer=self.word_list.data)


        hamming_dist = pdist(word_bytes, metric='hamming')

        matrix = squareform(hamming_dist < 1.5 / 3)

        self.graph = csr_matrix(matrix)


    def findingShortestPath(self,start,end):
        self.start  = self.word_list.searchsorted('start')
        self.end    = self.word_list.searchsorted('end')

        self.distances, self.predessors  = dijkstra(self.graph,indices=self.start,return_predecessors=True)

        return distances[self.end]




    def findingPath(self,start,end):
        path = []

        i = self.end

        while i != self.start:
            path.append(i)

            i = self.predessors[i]

        path.append(self.start)

        return path[::-1]


    def findingUniqueWord(self):
        N_components, compoent_list = connected_components(self.graph)

        unique = [ list(self.word_list[np.where(compoent_list==i)]) for i in range(1,N_components)]

        return unique





