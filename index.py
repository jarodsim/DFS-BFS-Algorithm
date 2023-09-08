import sys

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, source, destination):
        self.add_vertex(source)
        self.add_vertex(destination)
        self.graph[source].append(destination)
        self.graph[destination].append(source)

    def breadth_first_search(self, initial_vertex):
        visited = set()
        queue = [initial_vertex]
        connected_components = []

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                component = self.bfs(vertex, visited)
                connected_components.append(component)

        return connected_components

    def bfs(self, vertex, visited):
        component = []
        queue = [vertex]

        while queue:
            current_vertex = queue.pop(0)
            if current_vertex not in visited:
                visited.add(current_vertex)
                component.append(current_vertex)
                queue.extend(self.graph[current_vertex])

        return component

    def depth_first_search(self):
        visited = set()
        connected_components = []

        for vertex in self.graph:
            if vertex not in visited:
                component = self.dfs(vertex, visited)
                connected_components.append(component)

        return connected_components

    def dfs(self, vertex, visited):
        component = []
        stack = [vertex]

        while stack:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                visited.add(current_vertex)
                component.append(current_vertex)
                stack.extend(self.graph[current_vertex])

        return component

    def find_connected_components(self):
        visited = set()
        components = []

        for vertex in self.graph:
            if vertex not in visited:
                component = self.breadth_first_search(vertex)
                components.append(component)

        return components


def read_graph_from_file(file_path):
    graph = Graph()
    
    with open(file_path, 'r') as file:
        num_vertices = int(file.readline().strip())
        vertices = file.readline().strip().split()
        num_edges = int(file.readline().strip())
        
        for vertex in vertices:
            graph.add_vertex(vertex)
        
        for _ in range(num_edges):
            source, destination = file.readline().strip().split()
            graph.add_edge(source, destination)
    
    return graph

def read_graph_from_file(file_path):
    graph = Graph()
    
    with open(file_path, 'r') as file:
        num_vertices = int(file.readline().strip())
        vertices = file.readline().strip().split()
        num_edges = int(file.readline().strip())
        
        for vertex in vertices:
            graph.add_vertex(vertex)
        
        for _ in range(num_edges):
            source, destination = file.readline().strip().split()
            graph.add_edge(source, destination)
    
    return graph

if __name__ == "__main__":
    file_path = sys.argv[1]
    
    graph = read_graph_from_file(file_path)

    components_bfs = graph.find_connected_components()
    components_dfs = graph.depth_first_search()

    print("Connected Components (Breadth-First Search):")
    for i, component in enumerate(components_bfs):
        print(f"Component {i + 1}: {component}")

    print("\nConnected Components (Depth-First Search):")
    for i, component in enumerate(components_dfs):
        print(f"Component {i + 1}: {component}")

    count_bfs = len(components_bfs)
    count_dfs = len(components_dfs)

    print(
        f"\nQuantidade de Componentes Conexas (Busca em Largura): {count_bfs}")
    print(
        f"Quantidade de Componentes Conexas (Busca em Profundidade): {count_dfs}")
