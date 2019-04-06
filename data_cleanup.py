

hamming_dist = pdist(word_bytes, metric='hamming')

mat = squareform(hamming_dist < 1.5 / 3)

graph = csr_matrix(mat)

i1 = word_list.searchsorted('and')
i2 = word_list.searchsorted('dog')

distances, predessors = dijkstra(graph,indices=i1, return_predecessors=True)


print (distances[i2])

path = []

i = i2

while i != i1:
    path.append(word_list[i])
    i = predessors[i]

path.append(word_list[i1])


N_components, compoent_list = connected_components(graph)



unique = [ list(word_list[np.where(compoent_list==i)]) for i in range(1,N_components)]




###### Which Words are max seprated


distances, predessors = dijkstra(graph, return_predecessors=True)


max_distances = np.max(distances[~np.isinf(distances)])


print distances[np.where(distances == max_distances)]

print word_list[i1],word_list[i2] ,word_list[i3]

