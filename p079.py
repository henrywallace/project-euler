from collections import defaultdict
from functools import reduce

graph = defaultdict(set)
unique = set()
with open('p079_keylog.txt') as f:
    for a, b, c in map(str.strip, f.readlines()):
        graph[a].add(b)
        graph[a].add(c)
        graph[b].add(c)
        unique.update([a, b, c])

def find_path(graph):
    # Kahn 1962 topological sort
    l = []
    s = graph.keys() - reduce(set.union, graph.values())
    while len(s) > 0:
        n = s.pop()
        l.append(n)
        for m in tuple(graph[n]):
            graph[n].remove(m)
            if all(m not in v for v in graph.values()):
                s.add(m)
    return l

print(''.join(find_path(graph)))



