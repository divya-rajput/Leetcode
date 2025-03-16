class Graph(object):
    def __init__(self, size):
        if size < 1:
            raise Exception("Size cannot be negative")
        self.__adj = [[] for _ in range(size+1)]

    def add_undirected_edge(self, u, v):
        self.__adj[u].append(v)
        self.__adj[v].append(u)

    def add_edge(self, u, v):
        self.__adj[u].append(v)

    def number_connected_components(self):
        done = [0]*(len(self.__adj) + 1)
        count = 0
        for i in range(1, len(self.__adj)):
            if not done[i]:
                self.__dfs(i, done)
                count += 1
        return count
            
    
    def __dfs(self, n, done):
        done[n] = 1
        for neighbour in self.__adj[n]:
            if not done[neighbour]:
                self.__dfs(neighbour, done)
    
if __name__ == '__main__':
    g = Graph(10)
    g.add_undirected_edge(1, 2)
    g.add_undirected_edge(4, 5)
    g.add_undirected_edge(4, 7)
    print(g.number_connected_components())
