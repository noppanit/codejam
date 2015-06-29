'''
Input
0 2
/home/gcj/finals
/home/gcj/quals
'''
'''
graph = {
        "a": ["b", "c"],
        "b" : ["b"]
        }
'''

def traverse_graph(graph, count=1):
    for k,v in graph.iteritems():
        for node in v:
            count += 1

    return count

with open('./file-fix-it/A-small-practice.in') as fp:
    lines = list(fp)
    start_with_line = 1
    for case in range(0, int(lines[0])):
        n_and_m = lines[start_with_line]
        array_of_n_and_m = n_and_m.split(" ")
        n = int(array_of_n_and_m[0])
        m = int(array_of_n_and_m[1])

        graph = {}
        until_line = start_with_line + (n+m) + 1
        for idx in range(start_with_line + 1, until_line):
            path = filter(None, lines[idx].split("/"))
            for idx, folder in enumerate(path):
                if len(path) > 1 and idx < len(path) - 1:
                    graph.setdefault(folder, set()).add(path[idx + 1].strip())
        
        start_with_line = until_line
        print graph
        print traverse_graph(graph)
        

                

#count = traverse_graph(graph)

#print count

    



