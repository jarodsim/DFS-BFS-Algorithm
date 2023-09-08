# testes para as funções
from index import Graph

# -------------- CASO 1 --------------
grafo1 = Graph()
grafo1.add_edge("A", "B")
grafo1.add_edge("B", "C")
grafo1.add_edge("C", "D")

componentes_largura1 = grafo1.find_connected_components()
componentes_profundidade1 = grafo1.depth_first_search("A")

print("Grafo 1:")
print("Componentes Conexas (Busca em Largura):")
for i, componente in enumerate(componentes_largura1):
    print(f"Componente {i + 1}: {componente}")

print("\nComponentes Conexas (Busca em Profundidade):")
for i, componente in enumerate(componentes_profundidade1):
    print(f"Componente {i + 1}: {componente}")

quantidade_largura1 = len(componentes_largura1)
quantidade_profundidade1 = len(componentes_profundidade1)

print(
    f"\nQuantidade de Componentes Conexas (Busca em Largura): {quantidade_largura1}")
print(
    f"Quantidade de Componentes Conexas (Busca em Profundidade): {quantidade_profundidade1}")

# -------------- CASO 2 --------------

grafo2 = Graph()
grafo2.add_edge("A", "B")
grafo2.add_edge("C", "D")
grafo2.add_edge("E", "F")

componentes_largura2 = grafo2.find_connected_components()
componentes_profundidade2 = grafo2.depth_first_search("A")

print("Grafo 2:")
print("Componentes Conexas (Busca em Largura):")
for i, componente in enumerate(componentes_largura2):
    print(f"Componente {i + 1}: {componente}")

print("\nComponentes Conexas (Busca em Profundidade):")
for i, componente in enumerate(componentes_profundidade2):
    print(f"Componente {i + 1}: {componente}")

quantidade_largura2 = len(componentes_largura2)
quantidade_profundidade2 = len(componentes_profundidade2)

print(
    f"\nQuantidade de Componentes Conexas (Busca em Largura): {quantidade_largura2}")
print(
    f"Quantidade de Componentes Conexas (Busca em Profundidade): {quantidade_profundidade2}")
# -------------- CASO 3 --------------

grafo3 = Graph()
grafo3.add_vertex("A")
grafo3.add_vertex("B")
grafo3.add_vertex("C")

componentes_largura3 = grafo3.find_connected_components()
componentes_profundidade3 = grafo3.depth_first_search("A")

print("Grafo 3:")
print("Componentes Conexas (Busca em Largura):")
for i, componente in enumerate(componentes_largura3):
    print(f"Componente {i + 1}: {componente}")

print("\nComponentes Conexas (Busca em Profundidade):")
for i, componente in enumerate(componentes_profundidade3):
    print(f"Componente {i + 1}: {componente}")

quantidade_largura3 = len(componentes_largura3)
quantidade_profundidade3 = len(componentes_profundidade3)

print(
    f"\nQuantidade de Componentes Conexas (Busca em Largura): {quantidade_largura3}")
print(
    f"Quantidade de Componentes Conexas (Busca em Profundidade): {quantidade_profundidade3}")
